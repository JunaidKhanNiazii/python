from fastapi import FastAPI

app = FastAPI() 

@app.get("/")
def read_root():
    return {"Hello" : "World"}


@app.get("/square/{number}")
def square_number(number:int):
    return {"number" : number, 
            "square" : number ** 2}