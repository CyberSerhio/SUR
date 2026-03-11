from sqlalchemy.sql.schema import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String

from setting import metadata


body_part = Table(
    "body_part",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(24), nullable=False),
)