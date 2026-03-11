from sqlalchemy.sql.schema import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Boolean, Text

from setting import metadata


npc_dialog = Table(
"npc_dialog",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("npc_id", Integer, ForeignKey("npc.id")), # чьи это реплики
    Column("first", Boolean, default=False, index=True), # если true то это первая реплика npc
    Column("quest_id", Integer, ForeignKey("quest.id"), nullable=True), # если в этой реплике есть квест который можно взять
    Column("text", Text, nullable=False),
    Column("answer", Boolean, default=False), # есть ли ответы на данную реплику, для игрока
    Column("to_save", Boolean, default=False), # если true то id этой реплики сохранаеться у персонажа и при следуюшем обращении персонажа он начинает c неё
    Column("next_dialog_id", Integer, ForeignKey("npc_dialog.id"), nullable=True), # следующая реплика npc если answer False, если True то следующая реплика из таблиици answer
)