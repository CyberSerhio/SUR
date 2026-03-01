from asyncio import run

from fastapi import FastAPI
import uvicorn
from sys import argv
from api.routers import include_all_api
from database.migrate import migrate
from setting import getenv

app = FastAPI()

include_all_api(app)

if __name__ == "__main__":
    try:
        arg = argv[1]
        if arg == "--migrate":
            run(migrate())
    except IndexError:
        uvicorn.run(app, host=getenv("FASTAPI_HOST"), port=int(getenv("FASTAPI_PORT")))