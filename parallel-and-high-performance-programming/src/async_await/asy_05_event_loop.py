import asyncio

"""
=========================================================
TOPIC: Event Loop

PURPOSE:
--------
Demonstrate how the Event Loop controls coroutine
execution in AsyncIO.

KEY IDEA:
---------
The Event Loop is the scheduler that:

1. Starts coroutines
2. Suspends coroutines at await points
3. Runs other coroutines while waiting
4. Resumes paused coroutines
5. Closes when all tasks finish

=========================================================

EXECUTION FLOW

main()
   ↓
Event Loop starts
   ↓
worker() starts
   ↓
worker sleeps
   ↓
Event Loop waits
   ↓
sleep finishes
   ↓
worker resumes
   ↓
worker ends
   ↓
Event Loop closes

=========================================================
"""


async def worker():

    """
    Simulates an I/O operation.

    The coroutine will pause for 5 seconds.
    """

    print("Worker started")

    print("Worker going to sleep")

    # Coroutine pauses here
    await asyncio.sleep(5)

    print("Worker resumed")

    print("Worker finished")


async def main():

    print("Main started")

    await worker()

    print("Main finished")


# Creates Event Loop automatically
asyncio.run(main())