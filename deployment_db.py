from sqlalchemy import create_engine # cretae engine is how sqlalchemy connects to your databse , think of it as bridge between python code and (orm) and the actual database (here postgresql) 
from sqlalchemy.orm import declarative_base, sessionmaker # sqlalchemy.orm is a subpackage of sqlalchemy that gives us orm specific tools like models , sessions , and declarative classes.
import os 
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL =  os.getenv("DATABASE_URL") # a way to get database url from the .env file.

engine = create_engine(DATABASE_URL)
sessionlocal = sessionmaker(bind=engine , autoflush=False )
# here you are saying give me a factory that makes session objects , a session is how sqlalchemy sends query to database 
# why you autocommit = false , u want to cntrl  whn the data is actually saved to the database (commited)
# same is for flush , you control the flow of data , data won't be sent automatically to database without your permission

Base = declarative_base()
# we can eventually link it to sqlite think of conn = sqlite3.connect(".......") here it's engine = create_engine("........")
# there cursor = conn.cursor() , here  here session = sessionlocal() , there cursor.execute() , here (session.add() , session.query()) ,
# there conn.commit() , here session.commit()
 




