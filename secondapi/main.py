from fastapi import FastAPI , Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()


my_posts = [{'name': 'bikash', 'class':2, 'id':1}, {'name':'Dipesh', 'class':1, 'id':2}]
class Post(BaseModel):
    title: str  # Correct usage of type annotations
    content: str  # Correct usage of type annotations
    published: bool = True  # Correct usage of default value
    rating: Optional[int] = None 

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p



@app.get("/")
async def root():
    return {"message": "Welcome to my API"}


@app.get("/posts")
async def get_posts():
    return { 'data': my_posts}



@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/{id}")
def get_post(id : int, response : Response):
    post = find_post(int(id))
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Post with id {id} is not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message" : f"Post with id:{id} is not found"}
    return {'post detail': post}

@app.delete("/posts/{id}")
# def delete_post():
    