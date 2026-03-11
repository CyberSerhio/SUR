from sqlalchemy.sql.schema import Table, Column, ForeignKey, UniqueConstraint
from sqlalchemy.sql.sqltypes import Integer, SmallInteger

from setting import metadata


item_attr_depend = Table(
    'item_attr_depend',
    metadata,
    Column("id", Integer, primary_key=True),
    Column('item_id', Integer, ForeignKey('item.id'), index=True),
    Column("attr_id", Integer, ForeignKey('attribute.id')),
    Column("count", SmallInteger, default=0),
    UniqueConstraint('item_id', 'attr_id')
)