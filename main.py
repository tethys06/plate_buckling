from typing import Union
from fastapi import FastAPI, Response
from pydantic import BaseModel
from PlateBuckling import Inputs
import json
import numpy as np

class Item(BaseModel):
    data: dict


app = FastAPI()

@app.get("/")
async def load_form():
    with open('Form.html') as fh:
        data = fh.read()
    return Response(content=data, media_type="text/html")

@app.get("/css/style.css")
async def load_css():
    with open('css/style.css') as fh:
        data = fh.read()
    return Response(content=data, media_type="text/css")


@app.post("/inputs/")
async def create_item(item: Item):
    data = Inputs(**item.data)
    result = data.CompressionBucklingAllowable()

    return json.dumps({'Fccr':f'{result:.0f}'})

'''
Need two endpoints
1 to serve html file
2 to take the config file

return a status code, then the result.

'''