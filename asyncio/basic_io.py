import asyncio

async def say_after(delay, prompt):
    print("program has started")
    await asyncio.sleep(delay)

    print(prompt)

asyncio.run(say_after(2, "Hello world"))