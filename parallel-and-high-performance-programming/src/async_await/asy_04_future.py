import asyncio

"""
=========================================================
TOPIC: AsyncIO Future

PURPOSE:
--------
A Future acts as a placeholder for a value that
will be available later.

It allows one coroutine to produce a result and
another coroutine to wait for it.

A Future is an awaitable object.

=========================================================
REAL WORLD ANALOGY
=========================================================

Future = Restaurant Token

You order food
       ↓
Receive token
       ↓
Food not ready yet
       ↓
Wait
       ↓
Food becomes available
       ↓
Receive food

The Future stores the future result.

=========================================================
"""


# --------------------------------------------------------
# PRODUCER COROUTINE
# --------------------------------------------------------
async def get_result(future):
    """
    Simulates a long operation.

    BEHAVIOR:
    ---------
    Waits 5 seconds and then places
    a result into the Future.
    """

    print("Producer started")

    # Simulate slow I/O operation
    await asyncio.sleep(5)

    print("Result generated")

    # Store result inside Future
    future.set_result(
        "Hello from Future!"
    )


# --------------------------------------------------------
# MAIN COROUTINE
# --------------------------------------------------------
async def main():

    print("Creating Future")

    # Create Future object
    my_future = asyncio.Future()

    print(
        "Future created "
        "(state = pending)"
    )

    # Schedule producer coroutine
    task = asyncio.create_task(
        get_result(my_future)
    )

    print(
        "Producer running "
        "in background..."
    )

    print(
        "\nWaiting for future value...\n"
    )

    # Wait until Future receives value
    result = await my_future

    print("Future completed")

    print(f"Received: {result}")

    await task

    print("\nProgram finished")


asyncio.run(main())