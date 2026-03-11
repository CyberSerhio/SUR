from sqlalchemy.sql.schema import Table, Column, ForeignKey, UniqueConstraint
from sqlalchemy.sql.sqltypes import Integer, SmallInteger

from setting import metadata


item_improve_item = Table(
    'item_improve_item',
    metadata,
    Column("id", Integer, primary_key=True),
    Column('item_id', Integer, ForeignKey('item.id'), index=True),
    Column("attr_id", Integer, ForeignKey('attribute.id')),
    Column("count", SmallInteger, default=0),
    UniqueConstraint('item_id', 'attr_id')
)