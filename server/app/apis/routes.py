from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.utils.db import get_collection

router = APIRouter()
users_collection = get_collection("users")
user_db = User(users_collection)

@router.post("/auth/signup")
async def signup(user: dict):
    if user_db.find_user_by_email(user["email"]):
        raise HTTPException(status_code=400, detail="User already exists.")

    user_db.create_user(user) 
    return {"message": "User registered successfully"}
