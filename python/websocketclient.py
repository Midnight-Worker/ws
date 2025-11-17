import asyncio
import websockets

i = 0

def setup():
    print("Startklar")

def loop():
    pass


async def on_message(msg):
    print("EVENT:", msg)



async def main():
    setup()

    async with websockets.connect("ws://ws.midnight-worker.de:3333") as ws:

        async def receiver():
            async for msg in ws:
                await on_message(msg)

        async def logic():
            while True:
                loop()
                await asyncio.sleep(1)

        await asyncio.gather(receiver(), logic())

asyncio.run(main())
