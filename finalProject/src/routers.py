from fastapi import FastAPI
from .data import user_data
from .schemas import User

app = FastAPI()

@app.get("/")
async def home():
    return user_data

@app.get("/user")
async def read_user(id: int):
    user = user_data.get(id)
    return user
