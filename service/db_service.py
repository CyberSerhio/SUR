from sqlalchemy.sql.expression import select, delete
from sqlalchemy import insert, update
from setting import SessionLocal
from setting import metadata


class DbService:

    @staticmethod
    def check_table(table_name: str):
        """ПРоверяем есть ли такая таблица в созданых нами таблицах"""
        table = metadata.tables[table_name]
        if table_name not in metadata.tables:
            raise ValueError("Table not found")
        return table

    async def all(self, table_name: str):
        table = self.check_table(table_name)
        async with SessionLocal() as session:
            result = await session.execute(select(table))
            return result.mappings().all()


    async def find_by(self, table_name: str, column: str, value):
        table = self.check_table(table_name)
        async with SessionLocal() as session:
            result = await session.execute(
                select(table).where(getattr(table.c, column) == value)
            )
            return result.mappings().all()

    async def create(self, table: str, value: dict = None):
        table = self.check_table(table)
        async with SessionLocal() as session:
            res = await session.execute(insert(table).values(**value).returning(table)
                                        if value else insert(table).returning(table))
            await session.commit()
            return res.mappings().all()

    async def create_all(self, table: str, value: list = None):
        table = self.check_table(table)
        async with SessionLocal() as session:
            await session.execute(insert(table).values(value))
            await session.commit()

    async def update(self, table: str, where: dict, value: dict):
        table = self.check_table(table)
        async with SessionLocal() as session:
            await session.execute(
                update(table)
                .where(*[getattr(table.c, k) == v for k, v in where.items()])
                .values(**value)
            )
            await session.commit()

    async def delete(self, table: str, where: dict):
        table = self.check_table(table)
        async with SessionLocal() as session:
            await session.execute(
                delete(table)
                .where(*[getattr(table.c, k) == v for k, v in where.items()])
            )
            await session.commit()