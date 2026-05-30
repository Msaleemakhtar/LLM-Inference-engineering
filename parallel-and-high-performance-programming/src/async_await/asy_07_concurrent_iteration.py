import asyncio
import random

"""
=========================================================
TOPIC: Concurrent Iteration using as_completed()
=========================================================

PURPOSE:
--------
Run multiple coroutines concurrently and
receive results immediately when each finishes.

IMPORTANT:
----------
Results arrive in completion order,
not submission order.

=========================================================
"""


async def worker(i):

    """
    Simulates a task with random duration.
    """

    delay = random.randint(1, 5)

    print(
        f"Task {i} started "
        f"(delay={delay})"
    )

    await asyncio.sleep(delay)

    print(f"Task {i} finished")

    return i


async def main():

    print("Launching tasks...\n")

    coroutines = [
        worker(i)
        for i in range(5)
    ]

    for completed in asyncio.as_completed(
        coroutines
    ):

        result = await completed

        print(
            f"Result received: {result}"
        )


asyncio.run(main())