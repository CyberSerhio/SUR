from sqlalchemy.sql.schema import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Text

from setting import metadata

news = Table("news", metadata,
             Column("id", Integer, primary_key=True),
             Column("title", String(256)),
             Column("description", Text),
             )
