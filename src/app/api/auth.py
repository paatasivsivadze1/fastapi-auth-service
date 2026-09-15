from fastapi import APIRouter
from app.api.dependencies import LoginForm,AuthService
from app.schemas.api.token import Token

router = APIRouter()


router.post('login')


@router.post('/login',response_model=Token)
async def login(auth_ser: AuthService,form_data : LoginForm):
    username , password = form_data.username,form_data.password
    jwt_token = await auth_ser.login_for_access_token(username, password)

    return Token(access_token=jwt_token,token_type="bearer")