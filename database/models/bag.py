from sqlalchemy.sql.schema import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Float

from setting import metadata


bag = Table(
    "bag",
    metadata,
    Column("id", Integer, primary_key=True),
)
