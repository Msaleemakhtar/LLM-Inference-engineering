"""
PURPOSE:
--------
This program demonstrates the Producer–Consumer problem
using a thread-safe Queue in Python.

BEHAVIOR:
---------
1. Two Producer threads generate random numbers.
2. Two Consumer threads retrieve numbers from the Queue.
3. Producers push data into the Queue using put().
4. Consumers safely fetch data using get().
5. Queue automatically handles synchronization between threads.

WHY THIS WORKS CORRECTLY:
-------------------------
- Queue is thread-safe (built-in locking internally)
- No shared variable is needed
- No Event or manual synchronization is required
- Each produced item is consumed exactly once
- No data loss or race conditions occur

KEY INSIGHT:
------------
👉 Queue = Producer–Consumer made easy

It internally provides:
- Locking
- Signaling
- Ordering (FIFO)
- Safe communication
"""

from threading import Thread
from queue import Queue
import time
import random

# Thread-safe shared queue (handles synchronization internally)
queue = Queue()

# Number of iterations per thread
count = 5


class Consumer(Thread):
    def __init__(self, count):
        Thread.__init__(self)
        self.count = count

    def run(self):
        global queue

        for i in range(self.count):

            # Blocks until an item is available in the queue
            local = queue.get()

            print("consumer has used this: %s" % local)

            # Notify queue that task is completed
            queue.task_done()


class Producer(Thread):
    def __init__(self, count):
        Thread.__init__(self)
        self.count = count

    def request(self):
        # Simulate production delay
        time.sleep(1)
        return random.randint(0, 100)

    def run(self):
        global queue

        for i in range(self.count):

            # Produce data
            local = self.request()

            # Put data into queue (thread-safe operation)
            queue.put(local)

            print("producer has loaded this: %s" % local)


# Create Producer threads
t1 = Producer(count)
t2 = Producer(count)

# Create Consumer threads
t3 = Consumer(count)
t4 = Consumer(count)

# Start all threads
t1.start()
t2.start()
t3.start()
t4.start()

# Wait for all threads to finish producing/consuming
t1.join()
t2.join()
t3.join()
t4.join()