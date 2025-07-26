from fastapi import FastAPI , Depends , HTTPException
from sqlalchemy.orm import Session
import deployment_models , deployment_schemas
from deployment_db import sessionlocal , engine
from deployment_db import Base



app = FastAPI()

def create_book(db:Session , book: deployment_schemas.BookCreate):
    db_book = deployment_models.Book(title = book.title , author = book.author)
    db.add(db_book)
    db.commit()
    return db_book


def get_books(db:Session  ):
    return db.query(deployment_models.Book).all()

def get_book(db:Session , book_id : int):
    return db.query(deployment_models.Book).filter(deployment_models.Book.id == book_id).first()

def delete_book(db:Session , title:str):
    book = db.query(deployment_models.Book).filter(deployment_models.Book.title == title).first()
    if book:
        db.delete(book)
        db.commit()
        return book

@app.post("/books" , response_model= deployment_schemas.BookOut)
def create_book(db:Session , book: deployment_schemas.BookCreate):
    db_book = deployment_models.Book(title = book.title , author = book.author)
    db.add(db_book)
    db.commit()
    return db_book


Base.metadata.create_all(bind= engine)

