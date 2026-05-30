import asyncio
import time

"""
=========================================================
TOPIC: AsyncIO Tasks and Concurrent Execution
=========================================================

PURPOSE:
--------
This program demonstrates how AsyncIO Tasks allow multiple
coroutines to execute concurrently.

A Task is a wrapper around a coroutine that schedules it
for execution by the Event Loop.

Without Tasks:
    Coroutine 1 finishes
    -> Coroutine 2 starts
    -> Coroutine 3 starts

With Tasks:
    Coroutine 1, 2 and 3 start together.
    The Event Loop switches between them whenever they
    reach an 'await' statement.

---------------------------------------------------------

WHY USE TASKS?
--------------
Tasks allow us to:

1. Run multiple coroutines concurrently.
2. Improve performance for I/O-bound operations.
3. Avoid waiting for one coroutine to completely finish
   before starting another.

---------------------------------------------------------

SCENARIO:
---------
We create three coroutines:

Task-1 -> waits 10 seconds
Task-2 -> waits 4 seconds
Task-3 -> waits 3 seconds

Since all are started concurrently:

Task-3 finishes first
Task-2 finishes second
Task-1 finishes last

Total execution time ≈ 10 seconds

NOT:

10 + 4 + 3 = 17 seconds

because they overlap their waiting periods.

---------------------------------------------------------

EVENT LOOP BEHAVIOR:
--------------------

Time ----->

Task-1 : START -------------------- END (10s)

Task-2 : START ------ END (4s)

Task-3 : START --- END (3s)

While one task is sleeping,
the Event Loop runs another task.

=========================================================
"""


# --------------------------------------------------------
# Coroutine
# --------------------------------------------------------
async def other(delay):
    """
    Simulates an I/O operation.

    PARAMETERS:
    ----------
    delay : number of seconds to wait

    BEHAVIOR:
    ---------
    1. Coroutine starts.
    2. Sleeps asynchronously.
    3. Retrieves current task name.
    4. Prints completion message.

    IMPORTANT:
    ----------
    asyncio.sleep() is NON-BLOCKING.

    During sleep:
        - This coroutine pauses.
        - Event Loop can run other coroutines.
    """

    print(f"[Task {asyncio.current_task().get_name()}] START")

    # Pause coroutine without blocking Event Loop
    await asyncio.sleep(delay)

    # Obtain current task object
    current_task = asyncio.current_task()

    # Read task name assigned during creation
    task_name = current_task.get_name()

    print(
        f"[Task {task_name}] "
        f"FINISHED after waiting {delay} seconds"
    )


# --------------------------------------------------------
# Main Coroutine
# --------------------------------------------------------
async def main():
    """
    Main coroutine.

    RESPONSIBILITIES:
    -----------------
    1. Create tasks.
    2. Start execution timer.
    3. Wait for all tasks to finish.
    4. Display total execution time.

    IMPORTANT:
    ----------
    create_task() immediately schedules the coroutine.

    It does NOT wait.

    All three tasks begin execution concurrently.
    """

    print("\nCreating Tasks...\n")

    # Start timing
    start_time = time.perf_counter()

    # Create Task objects
    task1 = asyncio.create_task(
        other(10),
        name="1"
    )

    task2 = asyncio.create_task(
        other(4),
        name="2"
    )

    task3 = asyncio.create_task(
        other(3),
        name="3"
    )

    print("All tasks have been scheduled.\n")

    # Wait for tasks to finish
    await task1
    await task2
    await task3

    # Stop timing
    end_time = time.perf_counter()

    elapsed = end_time - start_time

    print("\n================================")
    print("ALL TASKS COMPLETED")
    print(f"Elapsed Time: {elapsed:.2f} seconds")
    print("================================")


# --------------------------------------------------------
# Program Entry Point
# --------------------------------------------------------
"""
asyncio.run()

1. Creates Event Loop
2. Executes main() coroutine
3. Runs scheduled tasks
4. Closes Event Loop when finished
"""
asyncio.run(main())