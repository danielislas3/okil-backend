from fastapi import FastAPI
from app.api.v1.endpoints.user import router as user_router
from app.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME)

    app.include_router(
        user_router, prefix=f"{settings.API_VERSION}/users", tags=["users"]
    )

    @app.get("/")
    def read_root():
        return {"message": f"Welcome to {settings.PROJECT_NAME}"}

    @app.get("/health")
    def health_check():
        return {"status": "healthy"}

    return app


app = create_app()
