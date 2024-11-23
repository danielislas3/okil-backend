from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User

router = APIRouter()


@router.get("/")
def get_users(db: Session = Depends(get_db)):
    try:
        users = db.query(User).all()
        return {
            "users": [
                {"id": user.id, "name": user.name, "email": user.email}
                for user in users
            ]
        }
    except Exception as e:
        return {"error": str(e)}
