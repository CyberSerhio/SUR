
from sqlalchemy.sql.schema import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Boolean

from setting import metadata

user_state_dialog = Table(
    "user_state_dialog",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("npc_id", Integer, ForeignKey("npc.id"), nullable=False), # находим по npc
    Column("user_id", Integer, ForeignKey("user.id"), nullable=False), # нахоидм по user
    Column("dialog_id", Integer, ForeignKey("npc_dialog.id"), nullable=True), # и выводим пользователю данную реплику
)