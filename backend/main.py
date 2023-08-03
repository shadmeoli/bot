import logging
from datetime import datetime

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Some pet bot",
    description="I am just extending on a pet project\nNothing sirious",
    version="0.2.0",
    redoc_url="/redoc",
    contact={"name": "Shadrack Meoli"},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[*],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/', tags="to_nothing_route")
async def to_nothing():

    return {
        "Nothing" : "Here"
    }




if __name__ == "__main__":
    try:
        uvicorn.run("main:app", host="0.0.0.0", reload=True)
    except Exception as err:
        logging.error(err)