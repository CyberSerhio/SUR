
from sqlalchemy.sql.schema import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Float, Text, String, SmallInteger

from setting import metadata


item = Table(
    "item",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("weight", Float, nullable=False), # каждая вещь имеет вес, для расчета сколько может утянуть игрок
    Column("profession_id", Integer, ForeignKey("profession.id")), # некоторыми вещами может пользоваться только определённая професия, если профессия не подойдёт то ответ "и что мне делать с этим?"
    Column("title", String(56), nullable=False),
    Column("description", Text, nullable=False),
    Column("price", Float, nullable=False),
    Column("img_path", String(255), nullable=False),
    Column("can_wear", Integer, ForeignKey("body_part.id"), nullable=True),
    # Зависимость от атрибутов и какие атрибуты прибавляет данная ващь в соответствующих таблицах
)