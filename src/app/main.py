
import app.api as routes
import app.models
from app.core.database import AsyncDB, db
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from app.core.config import settings

class MainApp:
    def __init__(self, db: AsyncDB):
        self.db = db
        self.app = FastAPI(lifespan=self.db.create_database_lifespan)

app_fastapi = MainApp(db).app


app_fastapi.add_middleware(
    SessionMiddleware,
    secret_key=settings.SECRET_KEY_FOR_OAUTH.get_secret_value(),
    https_only=False,
    same_site="lax"
)
app_fastapi.include_router(routes.routers)

def main():
    import uvicorn
    uvicorn.run("app.main:app_fastapi", host="127.0.0.1", port=8000, reload=True)