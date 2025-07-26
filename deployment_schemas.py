from pydantic import BaseModel

class BookBase(BaseModel):
    title:str
    author:str

class BookCreate(BookBase): #this class inherits from BookBase  , meaning it includes the same fields , title and author , pass means do nothing , it just extends bookbase without adding anything new , why this class , exists ? often in real apps you might later add creation specific fields , like price , summary etc , so it gives flexibility.
    pass

class BookOut(BookBase):
    id: int # this class also inherits from BookBase class so it already has title and author , but now it adds an extra field : id (usually  the DB id of the book)
    # it's used when returning data from the api so that user can see the id along with the title and author.


class Config:
    orm_mode = True    
    #  orm_mode = True   , tells pydantic , hey , it's okay if i get sqlalchemy model objects . i'll convert them into json , without this fastapi would crash when you try to return a book model object.
    # this tells pydantic that this model is going to work with orm objects ( like sqlalechemy models), with this pydantic allows this model to read data from sqlalchemy models or any class with attributes (not just dicts)


    