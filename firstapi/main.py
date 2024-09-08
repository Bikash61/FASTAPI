from fastapi import FastAPI

app = FastAPI()
@app.get("/")
@app.post("/")

async def read_item():
    return {'a': ['item1','item2','item3']}


async def read_a_line():
    return {'bikash': ['Handsome', 'lovable', 'better']}
