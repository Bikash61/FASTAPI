from fastapi import FastAPI

app = FastAPI()
@app.get("/")

async def root():
    return {'messages': "Welcome to my API"}

@app.get('/post')    
def get_post():
    return {'title': 'My Post', 'content': 'This is my post'}