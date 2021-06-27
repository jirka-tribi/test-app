import aiohttp
import pytest
from test1.test2.test3.app import App


@pytest.mark.asyncio
async def test_status(operators_api: App) -> None:
    # pylint: disable=unused-argument
    async with aiohttp.ClientSession() as session:
        async with session.get("http://localhost:8080/status") as response:
            assert response.status == 200
