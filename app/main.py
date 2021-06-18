from typing import Dict

import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from fake_db import db
from utils import calculate_results

app = FastAPI(
    title="Async Server", docs_url="/api/docs", openapi_url="/api/openapi"
)


class BaseJsonModel(BaseModel):
    js: Dict


@app.get("/")
async def root():
    print(db)
    return {"message": "Hello World", "fake_db": db if True else None}


@app.post("/api/create")
async def post_json(js: BaseJsonModel):
    json_compatible_item_data = jsonable_encoder(js)
    db.append(json_compatible_item_data)
    return js


@app.get("/api/read")
async def read_item(sum: int = None):
    data = calculate_results(db[:sum])
    return data


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True, port=8000)
