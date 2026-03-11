from sqlalchemy.sql.schema import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Text, SmallInteger

from setting import metadata

quest = Table(
    "quest",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(256), nullable=False),
    Column("description", Text, nullable=False),
    Column("improve_exp", SmallInteger, nullable=False), # сколько опыта получит игрок за выполнение задания
    Column("quest_id", Integer, ForeignKey("quest.id"), nullable=True), # если указан, то оно должно быть завершено
    Column("profession_id", Integer, ForeignKey("profession.id"), nullable=True), # зависимость от професии
)