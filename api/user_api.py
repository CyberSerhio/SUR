
from fastapi import APIRouter, HTTPException

from database.req_data_models.create_user_query import CreateUserQuery
from database.req_data_models.login_query import LoginQuery
from service.db_service import DbService
from service.user_service import create_user, delete_user

user_router = APIRouter()
db_service = DbService()


@user_router.post("/login")
async def login(data: LoginQuery):
    user = await db_service.find_by("user","username" , data.username)
    print(user)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {
        "username": data.username,
    }

@user_router.post("/create")
async def create(data: CreateUserQuery):
    answer = await create_user(data)
    return answer

@user_router.post("/delete")
async def create(user_id: int):
    answer = await delete_user(user_id)
    return answer