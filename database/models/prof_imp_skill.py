from sqlalchemy.sql.schema import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, SmallInteger

from setting import metadata


profession_improve_skill = Table(
    "profession_improve_skill",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("profession_id", Integer, ForeignKey("profession.id"), nullable=False),
    Column("skill_id", Integer, ForeignKey("skill.id"), nullable=False),
    Column("count", SmallInteger, nullable=False),
)