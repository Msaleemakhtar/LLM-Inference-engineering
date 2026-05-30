"""
=========================================================
TOPIC: asyncio.gather()
=========================================================

PURPOSE:
--------
asyncio.gather() is used to execute multiple awaitable
objects concurrently and collect their return values.

Awaitables can be:
    - Coroutines
    - Tasks
    - Futures

If coroutines are passed to gather(), AsyncIO
automatically converts them into Tasks internally.

=========================================================
WHY USE GATHER?
=========================================================

Without gather():

    await coro1()
    await coro2()
    await coro3()

Execution:

    coro1 finishes
        ↓
    coro2 starts
        ↓
    coro3 starts

Behavior:
    Sequential execution

Total Time:
    t1 + t2 + t3

---------------------------------------------------------

With gather():

    await asyncio.gather(
        coro1(),
        coro2(),
        coro3()
    )

Execution:

    coro1 starts
    coro2 starts
    coro3 starts

All run concurrently.

Behavior:
    Concurrent execution

Total Time:
    Approximately the slowest coroutine

=========================================================
EXAMPLE TIMELINE
=========================================================

Coroutine A -> sleep(10)
Coroutine B -> sleep(4)
Coroutine C -> sleep(2)

Sequential:

Time →

AAAAAAAAAA
          BBBB
              CC

Total:
    10 + 4 + 2 = 16 sec

---------------------------------------------------------

Gather():

Time →

AAAAAAAAAA
BBBB
CC

Total:
    ≈ 10 sec

=========================================================
GATHER VS CREATE_TASK
=========================================================

create_task():

    task1 = asyncio.create_task(coro1())
    task2 = asyncio.create_task(coro2())

Advantages:
    ✔ Task object available
    ✔ Can cancel tasks
    ✔ Can check status
    ✔ Better control

Disadvantages:
    ✘ More code

---------------------------------------------------------

gather():

    results = await asyncio.gather(
        coro1(),
        coro2()
    )

Advantages:
    ✔ Cleaner syntax
    ✔ Automatically schedules tasks
    ✔ Returns results automatically
    ✔ Ideal when waiting for all tasks

Disadvantages:
    ✘ Less control over individual tasks

=========================================================
COMPARISON TABLE
=========================================================

1. Sequential Coroutines

    await coro1()
    await coro2()
    await coro3()

    Concurrent?     NO
    Time?           Sum of all durations
    Returns?        Individual results

---------------------------------------------------------

2. create_task()

    task1 = create_task(coro1())
    task2 = create_task(coro2())

    Concurrent?     YES
    Time?           Slowest task
    Returns?        Individual task results
    Control?        Full

---------------------------------------------------------

3. gather()

    await gather(
        coro1(),
        coro2()
    )

    Concurrent?     YES
    Time?           Slowest task
    Returns?        List of results
    Control?        Limited

=========================================================
IMPORTANT OBSERVATION
=========================================================

Completion Order:

    C finishes first
    B finishes second
    A finishes last

Result Order:

    [A_result, B_result, C_result]

gather() ALWAYS preserves the order of the input
sequence, not the completion order.

=========================================================
EVENT LOOP BEHAVIOR
=========================================================

Time →

A : START ---------------- END (10s)

B : START ---- END (4s)

C : START -- END (2s)

While one coroutine is waiting at 'await',
the Event Loop runs another coroutine.

=========================================================
MEMORY TRICK
=========================================================

await coroutine()
    = Sequential Async

create_task()
    = Concurrent Async with Control

asyncio.gather()
    = Concurrent Async + Collect Results

=========================================================
"""
import asyncio
import time

"""
=========================================================
TOPIC: asyncio.gather()

PURPOSE:
--------
Run multiple coroutines concurrently and collect
their return values.

BENEFIT:
--------
Cleaner and shorter code than manually creating
and awaiting multiple tasks.

EVENT LOOP BEHAVIOR:
--------------------

Time →

Coroutine A : START ---------------- END (10s)

Coroutine B : START ---- END (4s)

Coroutine C : START -- END (2s)

All start together.

Total time ≈ 10 seconds

=========================================================
"""


async def coroutine(delay, task_id):
    """
    Simulates an I/O operation.

    PARAMETERS:
    ----------
    delay    -> sleep duration
    task_id  -> identifier

    RETURNS:
    --------
    delay + 2
    """

    print(f"[{task_id}] START")

    # Non-blocking sleep
    await asyncio.sleep(delay)

    print(f"[{task_id}] FINISHED")

    return delay + 2


async def main():

    print("Starting gather...\n")

    start = time.perf_counter()

    # Run all coroutines concurrently
    results = await asyncio.gather(
        coroutine(10, "A"),
        coroutine(4, "B"),
        coroutine(2, "C")
    )

    end = time.perf_counter()

    print("\nResults:", results)
    print(f"Elapsed Time: {end - start:.2f} sec")


asyncio.run(main())