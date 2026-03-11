from sqlalchemy.sql.schema import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, SmallInteger, Text, Boolean

from setting import metadata

room = Table(
    "room",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(100), nullable=True),
    Column("x", SmallInteger, nullable=False), # по оси Х относительно центра
    Column("y", SmallInteger, nullable=False), # по оси y относительно центра
    Column("root_room_id", Integer, ForeignKey("room.id"), nullable=True, default=None), # если идет переход например в здание, при выходе из него мы знаем куда вернуть игрока
    Column("wait_time", SmallInteger, nullable=True), # сколько в данной локации придётся провести персонажу стандартно
    Column("img_path", Text, nullable=True), # путь к бэкграунду комнаты
    Column("protect", Boolean, default=False), # если true то при нападении на другого персонажа в бой вступят защитники (неигровые персонажи максимальных характеристик)
    Column("mobs", Boolean, default=True), # если true то можно вступить в бой с мобами
)