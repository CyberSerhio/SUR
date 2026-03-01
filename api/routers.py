from api.server_api import router as server_api
from fastapi import FastAPI

def include_all_api(app: FastAPI):
    """:param app: FastAPI app - добавляем все роуты в аплицацию"""
    app.include_router(server_api)