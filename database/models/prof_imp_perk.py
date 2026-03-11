from sqlalchemy.sql.schema import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, SmallInteger

from setting import metadata


profession_improve_perk = Table(
    "profession_improve_perk",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("profession_id", Integer, ForeignKey("profession.id"), nullable=False),
    Column("perk_id", Integer, ForeignKey("perk.id"), nullable=False),
)