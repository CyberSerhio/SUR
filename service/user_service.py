from sqlalchemy import insert

from database.req_data_models.create_user_query import CreateUserQuery
from service.db_service import DbService
from setting import DEF_PATH

db_service = DbService()

async def create_user(data: CreateUserQuery):
    user = await db_service.find_by("user", "username", data.username)
    if not user:
        img_path = DEF_PATH + "/media/img/man0.jpg"
        bag = await db_service.create("bag")
        stash = await db_service.create("stash")
        if not data.man:
            img_path = DEF_PATH + "/media/img/girl0.jpg"
        user_data = {
            "username": data.username,
            "email": data.email,
            "phone": data.phone,
            "bag_id": bag[0].id,
            "stash_id": stash[0].id,
            "avatar_path": img_path,
        }
        user = await db_service.create("user", user_data)
        await create_user_attrs(user[0].id)
        return {"message": "User created successfully"}
    return {"message": "User already exists"}

async def delete_user(user_id: int):
    # Needs to auth
    user = await db_service.find_by("user", "id", user_id)
    if user:
        await db_service.delete("user", {"id": user_id})
        await db_service.delete("user_attr", {"user_id": user_id})
        await db_service.delete("bag", {"id": user[0].bag_id})
        return {"message": "User deleted successfully"}
    return {"message": "User does not exist"}

async def create_user_attrs(user_id: int):
    attrs = await db_service.all("attribute")
    data = [
        {
            "attr_id": attr.id,
            "user_id": user_id,
        }
        for attr in attrs
    ]

    await db_service.create_all("user_attr", data)