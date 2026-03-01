from sqlalchemy.sql.expression import select

from database.models.news import news
from setting import SessionLocal


async def get_news():
    async with SessionLocal() as session:
        result = await session.execute(select(news))
        return result.mappings().all()