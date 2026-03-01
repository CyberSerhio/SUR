from os import getenv
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.schema import MetaData

load_dotenv()

engine = create_async_engine(getenv("DATABASE_URL"), echo=True)
metadata = MetaData()

SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
