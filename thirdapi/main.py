# from fastapi import FastAPI
# from pydantic import BaseModel
# from datetime import datetime

# app = FastAPI()

# class Book(BaseModel):
#     title : str
#     book_number : int
#     author : str
#     page : int 

# book_details = []

# @app.get('books/')
# async def read_books()


#     return book_details

# @app.get('books/{id}')
# async def read_books():
#     return book_details[id]

# @app.post('books/')
# async def create_books(book : Book):
#     book_details.append(book)
#     return book_details


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    pages: int
    book_id: int

books = []

@app.post("/books")
async def create_book(book: Book):
    books.append(book)
    return book

@app.get("/books")
async def read_books():
    return books

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    if book_id < 0 or book_id >= len(books):
        return {"error": "Book not found"}
    return books[book_id]

@app.put("/books/{book_id}")
async def update_book(book_id: int, book: Book):
    if book_id < 0 or book_id >= len(books):
        return {"error": "Book not found"}
    books[book_id] = book
    return book

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    if book_id < 0 or book_id >= len(books):
        return {"error": "Book not found"}
    deleted_book = books.pop(book_id)
    return {"message": "Book deleted", "book": deleted_book}