from sqlalchemy.sql.schema import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Text

from setting import metadata


profession = Table("profession", metadata,
                   Column("id", Integer, primary_key=True),
                   Column("title", String(32)),
                   Column("description", Text),
                   Column("quest_depend", Integer, ForeignKey("quest.id")), # зависимость от стату выполненого задания
                   )