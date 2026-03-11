from sqlalchemy import Column, SmallInteger, ForeignKey
from sqlalchemy.sql.schema import Table
from sqlalchemy.sql.sqltypes import Integer

from setting import metadata

perk_improve_attr = Table(
    "perk_improve_attr",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("perk_id", Integer, ForeignKey("perk.id")),
    Column("attr_id", Integer, ForeignKey("attribute.id")),
    Column("count", Integer, nullable=True),
)