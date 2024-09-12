from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name : str
    age : int
    city:  str
    roll_no : int
    email : EmailStr


