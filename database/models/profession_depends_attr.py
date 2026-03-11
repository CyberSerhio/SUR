from sqlalchemy.sql.schema import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, SmallInteger

from setting import metadata

prof_depends_attr = Table("profession_depends_attr", metadata,
                     Column("id", Integer, primary_key=True),
                     Column("profession_id", Integer, ForeignKey("profession.id")),
                     Column("attribute_id", Integer, ForeignKey("attribute.id")),
                     Column("attr_count", SmallInteger, nullable=False)
                     )