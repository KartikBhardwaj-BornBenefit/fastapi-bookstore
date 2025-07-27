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

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()    

@app.get("/")
def read_root():
    return {"message" : FastAPI is "running"}



@app.post("/books" , response_model= deployment_schemas.BookOut)
def create_book( book: deployment_schemas.BookCreate  ,db:Session = Depends(get_db)):
    db_book = deployment_models.Book(title = book.title , author = book.author)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.get("/books", response_model= list[deployment_schemas.BookOut])
def get_books(db:Session = Depends(get_db)):
    return db.query(deployment_models.Book).all()



Base.metadata.create_all(bind= engine)

