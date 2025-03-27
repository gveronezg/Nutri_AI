import asyncio

async def main():
    await asyncio.sleep(1)
    print("Await funcionando!")

asyncio.run(main())