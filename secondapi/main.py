from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor


app = FastAPI()

# Define the Post model only once
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None  # Optional field


try:
    conn = psycopg2.connect(host = 'localhost', database = 'fastapi',user = 'postgres',password = 'root', cursor_factory= RealDictCursor)
    cursor = conn.cursor()


# Simulating a list of posts as an in-memory data store
my_posts = [
    {'title': 'Romeo', 'content': 'This is a Romeo Movie', 'id': 1},
    {'title': 'Rom', 'content': 'This is a Movie', 'id': 2},
]

# Function to find a post by ID
def find_post(id: int) -> Optional[dict]:
    for p in my_posts:
        if p['id'] == id:
            return p

# Function to find the index of a post by ID
def find_index_post(id: int) -> Optional[int]:
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i
    return None

@app.get("/")
async def root():
    return {"message": "Welcome to my API"}

@app.get("/posts")
async def get_posts():
    return {'data': my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)  # Assign a random ID
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} is not found")
    return {'post_detail': post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} does not exist")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
