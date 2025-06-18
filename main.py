from fastapi import FastAPI, Query
import math
from typing import List



app = FastAPI()

@app.get("/")
def home():
    return {"message" : "welcome to the word game API "}

@app.get("/student")
def avg(name  : str , marks : List[int] = Query(...) , subjects : List[str] = Query(...)):
    return {"name" : name, "marks": marks, "subjects": subjects , "avg": sum(marks)/len(subjects)}


    





