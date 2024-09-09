from fastapi import FastAPI
from fastapi.params import Body
app = FastAPI()
@app.get("/")

async def root():
    return {'messages': "Welcome to my API"}

@app.get('/sample')    
def sample():
    return {'title': 'My Post', 'content': 'This is my post'}



@app.post('/post')
async def post(payload : dict = Body(...)):
    print(payload)
    return {'newpost': f"Name {payload}"}     