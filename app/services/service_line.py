from decouple import config
from fastapi.responses import JSONResponse
import requests

class LineService:
    def __init__(self):
        self.line_host = config("LINE_HOST")

    def config(self, token):
        content = {"message": True}
        response = JSONResponse(content=content)
        response.set_cookie(key='token', value=token)
        return response

    def send_msg(self, token, subject, body):
        headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'Authorization':'Bearer ' + token
        }
        data = f'{subject}\n{body}' 
        response = requests.post(self.line_host, headers=headers, data = {'message': data})
        if response.status_code == 200:
            return response.json()
        else:
            return JSONResponse(status_code=response.status_code, content={"message": response.reason})