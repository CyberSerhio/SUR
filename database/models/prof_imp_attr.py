from sqlalchemy.sql.schema import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, SmallInteger

from setting import metadata


profession_improve_attr = Table(
    "profession_improve_attr",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("profession_id", Integer, ForeignKey("profession.id"), nullable=False),
    Column("attr_id", Integer, ForeignKey("attribute.id"), nullable=False),
    Column("count", SmallInteger, nullable=False),
)