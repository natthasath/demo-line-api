from fastapi import Form
from pydantic import BaseModel, Field, EmailStr, SecretStr
from typing import List, Union
import inspect

def form_body(cls):
    cls.__signature__ = cls.__signature__.replace(
        parameters=[
            arg.replace(default=Form(default = arg.default) if arg.default is not inspect._empty else Form(...))
            for arg in cls.__signature__.parameters.values()
        ]
    )
    return cls

@form_body
class ConfigSchema(BaseModel):
    token: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "token": "Incremental Number"
            }
        }

@form_body
class SendMessageSchema(BaseModel):
    subject: str = Field(...)
    body: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "subject": "Alert-Line",
                "body": "Hi this test message, thanks for using Line Notify"
            }
        }