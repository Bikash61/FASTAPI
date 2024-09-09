from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str  # Correct usage of type annotations
    content: str  # Correct usage of type annotations
    published: bool = True  # Correct usage of default value
    rating: Optional[int] = None # Correct usage of default value
@app.get("/")
async def root():
    return {"message": "Welcome to my API"}

@app.post("/create")
def create_posts(new_post: Post):
    print(new_post.dict())
    print(new_post.published)
    return {"data": new_post}
