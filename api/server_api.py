from fastapi import APIRouter

from service.db_service import DbService

router = APIRouter()
db_service = DbService()

@router.get("/")
async def root():
    news = await db_service.all('news')
    return news


@router.get("/news")
async def root(title: str):
    news = await db_service.find_by('news', "title", title)
    return news