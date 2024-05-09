import asyncio


async def main():
    task = asyncio.create_task(other_function())
    return_value = await task
    # await task
    print("A")
    await asyncio.sleep(1)
    print("B")
    # await task
    print(f"Return Value was {return_value}")


async def other_function():
    print("1")
    await asyncio.sleep(2)
    print("2")
    return 10


asyncio.run(main())
