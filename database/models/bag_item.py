from sqlalchemy.sql.schema import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, SmallInteger, Boolean

from setting import metadata


bag_item = Table(
    "bag_item",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("bag_id", Integer, ForeignKey("bag.id"), nullable=False),
    Column("item_id", Integer, ForeignKey("item.id"), nullable=False),
    Column("count", SmallInteger, nullable=False, default=1), # может быть несколько предметов, например 5 паторонов
    Column("current_quality_state", SmallInteger, nullable=False, default=100), # состояние вещи сейчас
    Column("is_wear", Boolean, default=False),
    Column("real_capacity", SmallInteger, nullable=True, default=0),
)