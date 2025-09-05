from fastapi import FastAPI
from math_utils import add_numbers

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello CI/CD!"}


@app.get("/add")
def add(a: int, b: int):
    result = add_numbers(a, b)
    return {"result": result}