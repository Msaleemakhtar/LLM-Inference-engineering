"""
===========================================================
MULTIPROCESSING QUEUE COMMUNICATION (PRODUCER-CONSUMER)
===========================================================

DESCRIPTION
-----------
This program demonstrates communication between processes
using multiprocessing.Queue in Python.

In multiprocessing, processes DO NOT normally share memory.
Each process has its own:
    - Memory space
    - Variables
    - Python interpreter
    - Process ID (PID)

Because processes are isolated, they need a SAFE communication
mechanism to exchange data.

Python provides:
    1. Queue
    2. Pipe

This example uses Queue.

-----------------------------------------------------------
WHAT IS A QUEUE?
-----------------------------------------------------------

Queue is a FIFO (First In First Out) data structure.

FIFO means:
    First inserted item → First removed item

Example:

    put(10)
    put(20)
    put(30)

    get() → 10
    get() → 20
    get() → 30

The order is preserved.

-----------------------------------------------------------
WHY QUEUE IS IMPORTANT
-----------------------------------------------------------

Queue provides:
    ✔ Safe communication
    ✔ Synchronization
    ✔ Buffering
    ✔ Ordered data transfer

Internally Queue manages:
    - Locks
    - Semaphores
    - Pipes
    - Synchronization

Therefore we usually DO NOT need manual locks.

-----------------------------------------------------------
PRODUCER-CONSUMER MODEL
-----------------------------------------------------------

Producer:
    Creates/generates data

Consumer:
    Receives and uses data

Flow:

    Producer ───► Queue ───► Consumer

-----------------------------------------------------------
QUEUE BEHAVIOR
-----------------------------------------------------------

1. put(data)
    Adds data into queue

2. get()
    Removes data from queue

3. Blocking Behavior

    - If queue is EMPTY:
        get() waits until data arrives

    - If queue is FULL:
        put() waits until space becomes available

-----------------------------------------------------------
BUFFERING
-----------------------------------------------------------

If producer is faster than consumer:

    Producer speed > Consumer speed

Data accumulates safely inside queue.

No overwriting occurs.

-----------------------------------------------------------
LIMITATIONS OF QUEUE
-----------------------------------------------------------

1. Serialization Overhead
    Data is serialized (pickled) before transfer.
    Large objects become slower.

2. Higher Memory Usage
    Large queues consume RAM.

3. Slower Than Shared Memory
    Data copying occurs between processes.

4. Possible Deadlocks
    Incorrect design may freeze processes.

5. qsize() Not Reliable Everywhere
    On some operating systems,
    qsize() may not return exact results.

-----------------------------------------------------------
PROCESS FLOW
-----------------------------------------------------------

Main Process
    │
    ├── Creates Queue
    │
    ├── Starts Producer Process
    │
    ├── Starts Consumer Process
    │
    ▼
Producer Process
    │
    ├── Generates data
    ├── queue.put(data)
    ▼

+-------------------+
|       Queue       |
|   FIFO BUFFER     |
+-------------------+

    ▲
    ├── queue.get()
    │
Consumer Process
    │
    ├── Receives data
    ├── Processes data
    ▼

-----------------------------------------------------------
GOAL OF THIS PROGRAM
-----------------------------------------------------------

To demonstrate:
    ✔ Multiprocessing
    ✔ Inter-process communication
    ✔ Queue synchronization
    ✔ Producer-consumer architecture
    ✔ FIFO behavior
    ✔ Blocking behavior
===========================================================
"""

from multiprocessing import Process, Queue
import time
import random


# --------------------------------------------------------
# Consumer Process
# Receives data FROM the queue
# --------------------------------------------------------
class Consumer(Process):

    def __init__(self, count, queue):

        # Initialize parent Process class
        Process.__init__(self)

        # Number of items to consume
        self.count = count

        # Shared Queue object
        self.queue = queue

    def run(self):

        # Consume items count times
        for i in range(self.count):

            print(f"\n[Consumer] Waiting for data...")

            # ------------------------------------------------
            # get() removes item from queue
            #
            # IMPORTANT:
            # If queue is empty,
            # consumer automatically waits (blocks)
            # until producer adds data.
            # ------------------------------------------------
            local = self.queue.get()

            print(f"[Consumer] Received: {local}")

            # Simulate processing delay
            time.sleep(2)

            print(f"[Consumer] Used data: {local}")


# --------------------------------------------------------
# Producer Process
# Produces data and puts it into queue
# --------------------------------------------------------
class Producer(Process):

    def __init__(self, count, queue):

        Process.__init__(self)

        self.count = count
        self.queue = queue

    # Simulate data generation
    def request(self):

        # Simulate delay in production
        time.sleep(1)

        # Generate random integer
        return random.randint(0, 100)

    def run(self):

        for i in range(self.count):

            # Generate data
            local = self.request()

            print(f"\n[Producer] Produced: {local}")

            # ------------------------------------------------
            # put() inserts item into queue
            #
            # If queue becomes full:
            # producer waits automatically.
            # ------------------------------------------------
            self.queue.put(local)

            print(f"[Producer] Added to queue")


# --------------------------------------------------------
# Main Process
# --------------------------------------------------------
if __name__ == "__main__":

    print("\n========== MAIN PROCESS STARTED ==========\n")

    # ----------------------------------------------------
    # Create Queue
    #
    # Queue acts as communication channel
    # between producer and consumer.
    #
    # maxsize optional:
    # queue = Queue(maxsize=5)
    # ----------------------------------------------------
    queue = Queue()

    # Number of items to exchange
    count = 5

    # Create producer process
    p1 = Producer(count, queue)

    # Create consumer process
    p2 = Consumer(count, queue)

    print("[Main] Starting Producer and Consumer...\n")

    # Start producer process
    p1.start()

    # Start consumer process
    p2.start()

    # ----------------------------------------------------
    # join() makes main process WAIT
    # until child processes finish.
    # ----------------------------------------------------
    p1.join()
    p2.join()

    print("\n========== MAIN PROCESS FINISHED ==========")