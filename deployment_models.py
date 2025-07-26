from sqlalchemy import Column , Integer , String  
from deployment_db import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer , primary_key = True , index = True)
    title = Column(String , index = True , unique = True)
    author = Column(String , index = True)
    # what indexing truly does ? , when u do,  author = column(String , index = True) u are telling te databse hey i'll be often search for books by author so please prepare a fast access structure for that ,
    # so th DB creates a B-Tree or similarr structure behind the scene ,
    # my confusio was if we're indexing column the why we fetch by rows , 
    # actually we're not searching by rows , youre asking ( SELECT*FROM  books WHERE  author = 'Rowling';) 
    #  that means use the index on author (a column) , find  which rows has author as rowling  , fetch the wholw row for every match.