import asyncio
from unittest.mock import AsyncMock

from .database import Database
from .app import App
from .web import WebServer


def main() -> None:
    loop = asyncio.get_event_loop()

    pg_pool = AsyncMock()
    test_db = Database(pg_pool)

    app = App(test_db)
    web_server = WebServer(app)

    try:
        loop.run_until_complete(web_server.start_web_server())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        loop.run_until_complete(web_server.aclose())


if __name__ == "__main__":
    main()
