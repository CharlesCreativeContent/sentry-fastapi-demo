# main.py
from fastapi import FastAPI, Request

import sentry_sdk

sentry_sdk.init(
    dsn="https://05e7c2630bbb4cb7b85d45ddac2dffd9@o4505422686584832.ingest.sentry.io/4505422689075200",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
)

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
