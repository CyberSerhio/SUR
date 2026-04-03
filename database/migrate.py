from setting import engine, DEF_PATH
from database.models import *
from os import system

async def migrate() -> None:
    """При вызове создаёт таблици в БД."""
    system(f'psql -U postgres -f {DEF_PATH}/database/create_db.sql -W')
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)

    system(f'psql -U suradmin -d surdb -f {DEF_PATH}/database/default_data.sql -W')