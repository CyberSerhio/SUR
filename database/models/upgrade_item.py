from sqlalchemy.sql.schema import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, SmallInteger

from setting import metadata


upgrade_item = Table(
    "upgrade_item",
    metadata,
    Column("upgradable", Integer, ForeignKey("item.id"), index=True),
    Column("improvement", Integer, ForeignKey("item.id")),
    Column("count", SmallInteger, default=0, nullable=True),
)