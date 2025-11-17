import asyncio
from wsclient import WebSocketClient


async def main():
    client = WebSocketClient("ws://ws.midnight-worker.de:3333")

    async def handle_open(ws):
        print("OPEN")
        await ws.send("Hallo vom Client!")

    async def handle_message(ws, msg):
        print("MESSAGE:", msg)

    async def handle_close():
        print("CLOSE")

    client.on_open = handle_open
    client.on_message = handle_message
    client.on_close = handle_close

    await client.run()


if __name__ == "__main__":
    asyncio.run(main())
