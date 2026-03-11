from sqlalchemy.sql.schema import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Text

from setting import metadata


answers = Table(
    "answers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("dialog_id", Integer, ForeignKey("npc_dialog.id")), # к какому диалогу привязаны ответы игрока
    Column("text", Text, nullable=False),
    Column("next_dialog_id", Integer, ForeignKey("npc_dialog.id"), nullable=True), # какую реплику следующую скажет npc
)