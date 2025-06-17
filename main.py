from fastapi import FastAPI, Query
import math
from typing import List


app = FastAPI()

@app.get("/")
def home():
    return{"message": "welcome to the word game API "}

@app.get("/student_name_and_marks")
def avg(name:str , marks:list[int], subjects= list[str]):
    return{"name": name, "marks":marks, "subjects": subjects , "avg": sum(marks)/len(subjects)}
   

    





