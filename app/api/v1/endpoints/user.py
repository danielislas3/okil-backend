from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User as UserModel
from app.schemas.user import User

router = APIRouter()

@router.get("/", response_model=list[User])
def get_users(db: Session = next(get_db())):
    users = db.query(UserModel).all()
    return users