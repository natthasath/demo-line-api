from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import JSONResponse
from app.models.model_line import ConfigSchema, SendMessageSchema
from app.services.service_line import LineService

router = APIRouter(
    prefix="/line",
    tags=["LINE"],
    responses={404: {"message": "Not found"}}
)

@router.post("/config")
async def config(data: ConfigSchema = Depends(ConfigSchema)):
    return LineService().config(data.token)

@router.post("/send")
async def root(request: Request, data: SendMessageSchema = Depends(SendMessageSchema)):
    token = request.cookies.get("token")
    return LineService().send_msg(token, data.subject, data.body)