from fastapi import FastAPI
from blog import schemas, models
from blog.database import engine

app = FastAPI()

# Create all models' tables
models.Base.metadata.create_all(engine)

@app.post('/blog')
def create(request: schemas.Blog):  # Use schemas.Blog for the type hint
    return request
