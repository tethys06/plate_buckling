from typing import Union
from fastapi import FastAPI, Response
from pydantic import BaseModel
from PlateBuckling import Inputs
import json

class Item(BaseModel):
    data: dict


app = FastAPI()

@app.get("/")
async def load_form():
    with open('Index.html') as fh:
        data = fh.read()
    return Response(content=data, media_type="text/html")


@app.post("/inputs/")
async def create_item(item: Item):
    data = Inputs(**item.data)
    result = data.CompressionBucklingAllowable()

    return json.dumps({'Fccr':result})

'''
Need two endpoints
1 to serve html file
2 to take the config file

return a status code, then the result.

'''