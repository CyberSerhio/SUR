from sqlalchemy.sql.schema import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, SmallInteger

from setting import metadata


weapon_item = Table(
    "weapon_item",
    metadata,
    Column("item_id", Integer, ForeignKey("item.id"), index=True),
    Column("max_distance", SmallInteger, default=1, nullable=False), # дистанция для применения оружи, нож бльёт в соседнюю клетку. Снайперская винтовка на 20 клеток...
    Column("max_capacity", SmallInteger, default=0, nullable=True), # если это огнестрел, то обьём обоимы
)