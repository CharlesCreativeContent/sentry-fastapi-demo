# main.py
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello this will be the home page until i figure out how to display a webpage or redirect"}

@app.get("/pokemon/")
async def root():
    return {"message": "Hello pokemon"}

@app.get("/map/")
async def root():
    return {"message": "Hello map"}

@app.get("/items/{item_id}")
def read_root(item_id: str, request: Request):
    client_host = request.client.host
    return {"client_host": client_host, "item_id": item_id}
