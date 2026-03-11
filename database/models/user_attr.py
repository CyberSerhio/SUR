from sqlalchemy.sql.schema import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, SmallInteger

from setting import metadata


user_attr = Table(
    "user_attr",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("attr_id", Integer, ForeignKey("attribute.id")),
    Column("user_id", Integer, ForeignKey("user.id")),
    Column("count", SmallInteger, default=0),
)