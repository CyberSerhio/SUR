from fastapi import FastAPI
import uvicorn
from setting import getenv


app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host=getenv("FASTAPI_HOST"), port=int(getenv("FASTAPI_PORT")))