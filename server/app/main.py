from fastapi import FastAPI
from app.apis.routes import router

app = FastAPI()

@app.get("/")
async def root():
    return {'message': 'I like foo'}

app.include_router(router)
