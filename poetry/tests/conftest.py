import asyncio
from asyncio.events import AbstractEventLoop
from unittest.mock import AsyncMock

import pytest

from test1.test2.test3.database import Database
from test1.test2.test3.app import App
from test1.test2.test3.web import WebServer


@pytest.fixture(scope="session")
def event_loop(request):  # type: ignore
    # pylint: disable=unused-argument
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def operators_api(event_loop: AbstractEventLoop):  # type: ignore

    test_app = App(
        Database(AsyncMock()),
    )

    web = WebServer(test_app)

    event_loop.run_until_complete(web.start_web_server())
    yield test_app
    event_loop.run_until_complete(web.aclose())
