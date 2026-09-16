from fastapi import APIRouter
from starlette.requests import Request
from app.api.dependencies import AuthService, LoginForm
from app.schemas.api.token import Token
from app.Oauth2.oauth2 import oauth

router = APIRouter()


router.post('login')


@router.post('/login',response_model=Token)
async def login(auth_ser: AuthService,form_data : LoginForm):
    username , password = form_data.username,form_data.password
    jwt_token = await auth_ser.login_for_access_token(username, password)

    return Token(access_token=jwt_token,token_type="bearer")

@router.get("/google/login")
async def login_via_google(request: Request):
    redirect_uri = request.url_for('auth_via_google')
    return await oauth.google.authorize_redirect(request, redirect_uri)

@router.get("/google/authorize")
async def auth_via_google(request: Request,auth_ser:AuthService):
    token = await oauth.google.authorize_access_token(request)
    user_info = token.get("userinfo")
    jwt_token = await auth_ser.process_google_login(dict(user_info))
    return Token(access_token=jwt_token, token_type="bearer")