from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def home():
  return{"message": "welcome to the word game API "}

@app.get("/jumble")
def jumble_word(word: str):
  if len(word) <3:
    return {"error": "word too short"}
   chars = list(word)
  random.shuffle(chars)
  jumbled=''.join(chars)
    return{"original":word, "jumbled":jumbled}


