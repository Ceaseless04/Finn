from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse 
from app.utils.db import get_collection

router = APIRouter()
users_collection = get_collection("users")

@router.post("/auth/signup")
async def signup(user: dict):
    if users_collection.find_one({"email": user["email"]}):
        raise HTTPException(status_code=400, detail="User already exists.")

    users_collection.create_user(user) 
    return {"message": "User registered successfully"}
