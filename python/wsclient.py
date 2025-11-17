import asyncio
import websockets


class WebSocketClient:
    def __init__(self, url: str):
        self.url = url
        self.on_open = None
        self.on_message = None
        self.on_close = None
        self._ws = None

    async def run(self):
        async with websockets.connect(self.url) as ws:
            self._ws = ws

            if self.on_open is not None:
                await self.on_open(ws)

            try:
                async for msg in ws:
                    if self.on_message is not None:
                        await self.on_message(ws, msg)
            finally:
                if self.on_close is not None:
                    await self.on_close()

    async def send(self, msg: str):
        if self._ws is None:
            raise RuntimeError("WebSocket ist nicht verbunden")
        await self._ws.send(msg)
