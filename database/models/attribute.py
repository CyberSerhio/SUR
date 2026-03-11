from sqlalchemy.sql.schema import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String

from setting import metadata


attribute = Table(
    "attribute",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("description", String),
)

