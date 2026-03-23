from sqlalchemy.sql.schema import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, SmallInteger, Boolean, Text

from setting import metadata


user = Table(
    "user", metadata,
Column("id", Integer, primary_key=True),
    Column("username", String(24)),
    Column("email", String(32)),
    Column("phone", String(16)),
    Column("profession", Integer, ForeignKey("profession.id"), default=1),
    Column("is_online", Boolean, default=False),
    Column("avatar_path", Text, nullable=False, default=""),
    Column("room_id", Integer, ForeignKey("room.id"), nullable=False, default=2),
    Column("bag_id", Integer, ForeignKey("bag.id"), nullable=False),
    Column("stash_id", Integer, ForeignKey("stash.id"), nullable=True)
)