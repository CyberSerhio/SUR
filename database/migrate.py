from setting import engine, metadata
import database.models

async def migrate() -> None:
    """При вызове создаёт таблици в БД."""
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
