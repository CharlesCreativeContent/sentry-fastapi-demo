# main.py
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "output Message here"}
