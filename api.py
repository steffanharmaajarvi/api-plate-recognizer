from typing import BinaryIO

import requests
import os
from dotenv import load_dotenv
from pprint import pprint
from fastapi import FastAPI, File, UploadFile

load_dotenv()
# The API endpoint
base_url = "https://api.platerecognizer.com/v1/{}"


class ApiRequest:
    def recognize(self, img: BinaryIO):
        url = base_url.format("plate-reader")
        response = self.__request("POST", url, img)
        return response.json()

    def __request(self, method: str, url: str, file) -> requests.Response:
        return requests.request(
            method,
            url,
            files=dict(upload=file),
            headers={'Authorization': 'Token {}'.format(self.__getToken())}
        )

    def __getToken(self) -> str:
        return os.getenv('API_KEY')
