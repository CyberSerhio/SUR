from fastapi import APIRouter
from sqlalchemy.orm.session import Session

from database.db_getter import get_news

router = APIRouter()


@router.get("/")
async def root():
    news = await get_news()
    return news