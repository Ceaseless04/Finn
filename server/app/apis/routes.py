from fastapi import APIRouter 
from app.utils.db import test_connection

router = APIRouter()
@router.get("db/connection")
async def connection():
    test_connection()
