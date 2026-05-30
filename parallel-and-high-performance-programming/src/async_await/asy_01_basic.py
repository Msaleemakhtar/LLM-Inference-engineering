import asyncio

"""
=========================================================
DETAILED DESCRIPTION OF THIS PROGRAM
=========================================================

PURPOSE:
--------
This program demonstrates Python's AsyncIO model using:

1. Coroutines (async functions)
2. Sequential execution using 'await'
3. Concurrent execution using 'asyncio.create_task()'
4. Event loop behavior (how AsyncIO schedules tasks)

---------------------------------------------------------

KEY CONCEPTS SHOWN:

1. COROUTINES
   - Defined using 'async def'
   - Do NOT run immediately when called
   - Must be executed using:
        - asyncio.run()
        - await
        - asyncio.create_task()

---------------------------------------------------------

2. AWAIT
   - Pauses the current coroutine
   - Gives control back to event loop
   - Allows other coroutines to run during waiting

Example:
    await asyncio.sleep(2)

This does NOT block the entire program.
It only pauses the current coroutine.

---------------------------------------------------------

3. CREATE_TASK
   - Starts coroutine immediately
   - Runs it in the background (concurrently)
   - Does NOT wait for completion instantly

---------------------------------------------------------

4. EVENT LOOP BEHAVIOR
   - Single-threaded scheduler
   - Manages multiple coroutines
   - Switches between tasks at 'await' points

---------------------------------------------------------

5. EXECUTION FLOW IN THIS PROGRAM

STEP 1:
    - Task-1 runs sequentially using 'await'
    - Main coroutine waits until it finishes

STEP 2:
    - Task-2 and Task-3 start using create_task()
    - They run concurrently
    - Event loop switches between them while waiting

---------------------------------------------------------

REAL-WORLD ANALOGY:

- Event Loop = Manager
- Coroutines = Workers
- await = "I am waiting, give work to someone else"
- create_task = "Start this worker immediately"

=========================================================
"""


# --------------------------------------------------------
# COROUTINE FUNCTION (Worker Task)
# --------------------------------------------------------
async def worker(name, delay):
    """
    A simple coroutine that simulates an I/O task.

    PARAMETERS:
    ----------
    name   : Identifier of the task
    delay  : Time to simulate waiting (like network or disk I/O)

    BEHAVIOR:
    ---------
    1. Prints start message
    2. Waits asynchronously (non-blocking)
    3. Prints completion message

    IMPORTANT:
    ----------
    During 'await asyncio.sleep()', this coroutine PAUSES,
    allowing other coroutines to run.
    """

    print(f"[{name}] START")

    # Non-blocking wait:
    # While this task is sleeping, other tasks can execute
    await asyncio.sleep(delay)

    print(f"[{name}] END after {delay} sec")


# --------------------------------------------------------
# MAIN COROUTINE (Entry Point)
# --------------------------------------------------------
async def main():
    """
    MAIN FUNCTION (Event Loop Controller)

    This function demonstrates two execution styles:

    1. Sequential Execution:
       - Uses 'await'
       - One task completes fully before next starts

    2. Concurrent Execution:
       - Uses 'asyncio.create_task'
       - Multiple tasks run at the same time
    """

    print("\n==============================")
    print("STEP 1: SEQUENTIAL EXECUTION (await)")
    print("==============================\n")

    # ----------------------------------------
    # STEP 1: Sequential Execution
    # ----------------------------------------
    await worker("TASK-1 (sequential)", 2)

    print("\nTask 1 completed → moving to concurrency demo\n")

    print("==============================")
    print("STEP 2: CONCURRENT EXECUTION (create_task)")
    print("==============================\n")

    # ----------------------------------------
    # STEP 2: Concurrent Execution
    # ----------------------------------------

    # Task is scheduled immediately (background execution)
    task2 = asyncio.create_task(worker("TASK-2 (concurrent)", 3))
    task3 = asyncio.create_task(worker("TASK-3 (concurrent)", 1))

    print("TASK-2 and TASK-3 started concurrently...\n")

    # Main coroutine continues running while tasks execute

    # Wait for both tasks to finish
    await task2
    await task3

    print("\n==============================")
    print("ALL TASKS COMPLETED")
    print("==============================\n")


# --------------------------------------------------------
# PROGRAM ENTRY POINT
# --------------------------------------------------------
"""
asyncio.run():
-------------
- Creates event loop
- Runs 'main()' coroutine
- Closes event loop after completion

This is the standard way to start AsyncIO programs.
"""
asyncio.run(main())