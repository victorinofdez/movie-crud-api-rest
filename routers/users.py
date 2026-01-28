from fastapi import APIRouter, HTTPException
from repositories.base_repository import *
from models.user import User

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create_user(user: User):
    try:
        create("users", user.id, user.dict())
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{user_id}")
def get_user(user_id: int):
    user = get("users", user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user
