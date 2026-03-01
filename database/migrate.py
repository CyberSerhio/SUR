from database.models.news import news
from setting import engine, metadata


async def migrate() -> None:
    """При вызове создаёт таблици в БД."""
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
