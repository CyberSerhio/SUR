from sqlalchemy.sql.schema import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, SmallInteger, Boolean, Text

from setting import metadata


perk = Table("perk", metadata,
        Column("id", Integer, primary_key=True),
        Column("title", String(32), nullable=False),
        Column("description", Text, nullable=False),
        Column("profession_id", SmallInteger, ForeignKey("profession.id")), # зависимость от професии
        Column("perk_level", SmallInteger, nullable=True), # уровень перка
        Column("is_active", Boolean, default=False), # можно ли его юзать или он пассивный
        Column("do_time", SmallInteger, nullable=True), # сколько времени он будет длиться в секундах
        Column("recovery_time", SmallInteger, nullable=True), # сколько времени будет востанавливаться в секундах
)