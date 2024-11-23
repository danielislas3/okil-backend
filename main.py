from fastapi import FastAPI
from app.api.v1.endpoints.user import router as user_router

app = FastAPI()

app.include_router(user_router, prefix="/api/v1/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Cafeteria POS API"}