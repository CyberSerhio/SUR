from sqlalchemy.sql.schema import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Text

from setting import metadata


npc = Table(
    "npc",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), nullable=False),
    Column("profession_id", Integer, ForeignKey("profession.id")),
    Column("avatar_path", Text, nullable=False),
    Column("room_id", Integer, ForeignKey("room.id")),
)