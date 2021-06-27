import asyncpg


class Database:
    def __init__(self, pg_pool: asyncpg.pool.Pool):
        self.pg_pool = pg_pool

    async def some_query(self) -> None:
        async with self.pg_pool.acquire():
            pass
