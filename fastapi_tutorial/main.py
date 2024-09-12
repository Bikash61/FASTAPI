from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
#Instance of FastAPI 

app = FastAPI()

@app.get('/blog')
def index(limit = 10, published : bool = True, sort : Optional[str] = None):
    #Only get 10 published blog
    if published:
        return {'data':f'There are {limit} published blog  extracted fron the database'}
    else:
        return {'data':f'There are {limit} blog  extracted fron the database'}


class Blog(BaseModel):
    title : str
    body : str
    published : Optional[bool] = True

@app.post('/blog')
def create_blog(request:Blog):
    return {'data': f'Blog is created with {request.title} successfully'}





@app.get('/blog/unpublished')
def unpublish_blog():
    return {
        'data':{
            'title':'Unpublished Blog',
            'content':'This is unpublished blog'
        }
    }

@app.get('/blog/{id}')
def showblog(id :int):
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id = int):
    return {'data': {1,2}}

