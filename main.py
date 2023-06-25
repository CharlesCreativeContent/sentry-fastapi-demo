# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello this will be the home page until i figure out how to display a webpage or redirect"}

@app.get("/items/")
async def root():
    return {"message": "Hello Items"}

@app.get("/pokemon/")
async def root():
    return {"message": "Hello pokemon"}

@app.get("/map/")
async def root():
    return {"message": "Hello map"}