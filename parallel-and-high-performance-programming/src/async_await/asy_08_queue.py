import asyncio
import random

"""
=========================================================
TOPIC: AsyncIO Queue (Producer-Consumer)

PURPOSE:
--------
Demonstrates communication between
producer coroutines and consumer coroutines.

QUEUE ROLE:
-----------
Acts as a shared buffer between producers
and consumers.

Producers:
    Generate data

Consumers:
    Process data

=========================================================

ARCHITECTURE

 Producer 0 ----\
 Producer 1 -----\
 Producer 2 ------> Queue ---> Consumer 0
 Producer 3 -----/           \
                            ---> Consumer 1

=========================================================

IMPORTANT METHODS

queue.put(item)
    Add item to queue

queue.get()
    Remove item from queue

queue.task_done()
    Mark item as processed

queue.join()
    Wait until all items processed

=========================================================
"""


# ------------------------------------------------------
# PRODUCER
# ------------------------------------------------------
async def producer(name, queue):

    """
    Producer Coroutine

    Generates a random number.

    Waits that many seconds to simulate
    an I/O operation.

    Then inserts the value into the queue.
    """

    # Simulated work result
    n = random.randint(0, 9)

    print(
        f"[Producer {name}] "
        f"Generating value {n}"
    )

    # Simulate slow operation
    await asyncio.sleep(n)

    # Add item into queue
    await queue.put(n)

    print(
        f"[Producer {name}] "
        f"Added {n} to queue"
    )


# ------------------------------------------------------
# CONSUMER
# ------------------------------------------------------
async def consumer(name, queue):

    """
    Consumer Coroutine

    Runs forever.

    Waits until queue contains data.

    Processes received value.
    """

    while True:

        print(
            f"[Consumer {name}] "
            f"Waiting for data..."
        )

        # Wait for item
        item = await queue.get()

        print(
            f"[Consumer {name}] "
            f"Received {item}"
        )

        # Simulate processing
        await asyncio.sleep(item)

        print(
            f"[Consumer {name}] "
            f"Processed {item}"
        )

        # Notify queue item finished
        queue.task_done()


# ------------------------------------------------------
# MAIN
# ------------------------------------------------------
async def main():

    # Shared Queue
    q = asyncio.Queue()

    print("\nCreating Producers")

    producers = [
        asyncio.create_task(
            producer(i, q)
        )
        for i in range(4)
    ]

    print("Creating Consumers")

    consumers = [
        asyncio.create_task(
            consumer(i, q)
        )
        for i in range(2)
    ]

    print("\nStarting system...\n")

    # Wait until all producers finish
    await asyncio.gather(*producers)

    print(
        "\nAll producers finished."
    )

    # Wait until queue becomes empty
    await q.join()

    print(
        "All queue items processed."
    )

    # Stop consumers
    for c in consumers:
        c.cancel()

    print("Consumers cancelled.")


asyncio.run(main())