from sqlalchemy.sql.schema import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, SmallInteger

from setting import metadata


quest_reward = Table(
    "quest_reward",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("quest", Integer, ForeignKey("quest.id"), nullable=False), # какое задание
    Column("item", Integer, ForeignKey("item.id"), nullable=False), # что получит игрок за него
    Column("count", SmallInteger, nullable=False), # в каком кол-ве, например 30 стрел или 5 патронов 12 калибра
)