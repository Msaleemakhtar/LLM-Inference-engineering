import asyncio

"""
=========================================================
TOPIC: Asynchronous Iteration using async for
=========================================================

PURPOSE:
--------
Demonstrates how an asynchronous generator
works with async for.

IMPORTANT:
----------
async for is NOT concurrent.

It only allows the Event Loop to run other
tasks while waiting.

The iteration itself remains sequential.

=========================================================
"""


async def gen(n):
    """
    Asynchronous Generator

    Generates numbers from 0 to n-1.

    Before yielding each number,
    it waits for 1 second.
    """

    for i in range(n):

        print(f"Preparing value {i}")

        # Pause coroutine
        await asyncio.sleep(1)

        yield i


async def main():

    print("Starting async iteration\n")

    async for value in gen(5):

        print(f"Received: {value}")

    print("\nIteration completed")


asyncio.run(main())