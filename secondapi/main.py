from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
app = FastAPI()

class Post(BaseModel):
    title = str
    content = str



@app.get("/")
async def root():
    return {'messages': "Welcome to my API"}

@app.post('/create_post')    
def create_post(new_post : Post):
    print(new_post)
    return {'data': 'new post'}



@app.post('/post')
async def post(payload : dict = Body(...)):
    print(payload)
    return {'newpost': f"Name {payload['name']}"}     