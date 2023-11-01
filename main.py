from typing import Union, Annotated

from fastapi import FastAPI, File, UploadFile

from api import ApiRequest

app = FastAPI()
api = ApiRequest()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/upload")
async def upload_picture(file: UploadFile):
    return api.recognize(file.file)