from sqlalchemy.sql.schema import Table, Column
from sqlalchemy.sql.sqltypes import String, Integer

from setting import metadata


skill = Table(
    "skill",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(56), nullable=False), # по типу электроника, холодное оружие, стрельба...
    Column("description", String(512), nullable=False),
)