from aiohttp import web
from aiohttp.web_request import Request

from .app import App


class WebServer:
    def __init__(
        self,
        app: App,
        host: str = "0.0.0.0",
        port: int = 8080,
    ) -> None:
        self.app = app

        self.host = host
        self.port = port
        self.web_app = web.Application()
        self.runner = web.AppRunner(self.web_app, access_log=None)

        self.web_app.router.add_route("GET", "/status", self.get_status)

    async def start_web_server(self) -> None:
        await self.runner.setup()
        site = web.TCPSite(self.runner, self.host, self.port)
        await site.start()

    async def get_status(self, _: Request) -> web.Response:
        status = self.app.test_status()
        return web.json_response({"status": status}, status=status)

    async def aclose(self) -> None:
        await self.runner.shutdown()
        await self.runner.cleanup()
