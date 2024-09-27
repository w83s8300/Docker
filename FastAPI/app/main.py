from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, FastAPI"}
@app.get("/data/")
def getData():
    return {"data":[2,3,4]}

@app.get("/square/{number}")
def getData(number):
    number=int (number)
    return {"result":number+100}

