from sqlalchemy.sql.schema import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Float, SmallInteger

from setting import metadata

# Скрытое хранилище, где игрок может спрятать вещи
stash = Table(
    "stash",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("capacity", SmallInteger, nullable=False, default=100), # можно вместить определённое кол-во вещей будет высчитываться из расчета 1 = 1.0 item.weight
)
