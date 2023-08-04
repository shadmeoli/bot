import logging
from datetime import datetime

import uvicorn
from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, validator, ValidationError

from bot import get_response
from backend.bot import responses


app = FastAPI(
    title="Some pet bot",
    description="I am just extending on a pet project\nNothing sirious",
    version="0.2.0",
    redoc_url="/redoc",
    contact={"name": "Shadrack Meoli"},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatValues(BaseModel):
    message: str

    class Config:
        json_schema_extra = {
            "post_demo": {
                "message": "<! some user specifie message>",
            }
        }


@app.post("/api/v1/chat", status_code=status.HTTP_200_OK)
async def chat(packet: ChatValues):
    try:
        response = get_response(packet.message)
        response_data = dict(bot=response, created_at=datetime.now())

        return response_data

    except Exception as error:
        logging.error(error)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


if __name__ == "__main__":
    try:
        uvicorn.run("main:app", host="0.0.0.0", reload=True)
    except Exception as err:
        logging.error(err)
