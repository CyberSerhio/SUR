from database.req_data_models.create_user_query import CreateUserQuery
from service.db_service import DbService

db_service = DbService()

async def create_user(data: CreateUserQuery):
    user = await db_service.find_by("user", "username", data.username)
    if not user:
        bag = await db_service.create("bag")
        stash = await db_service.create("stash")
        user_data = {
            "username": data.username,
            "email": data.email,
            "phone": data.phone,
            "bag_id": bag[0].id,
            "stash_id": stash[0].id
        }
        await db_service.create("user", user_data)
    return {"message": "User already exists"}

async def delete_user(user_id: int):
    user = await db_service.find_by("user", "id", user_id)
    if user:
        await db_service.delete("user", {"id": int(user_id)})
        return {"message": "User deleted successfully"}
    return {"message": "User does not exist"}

# async def update_user(user_id: int):
#     user = await db_service.find_by("user", "id", user_id)