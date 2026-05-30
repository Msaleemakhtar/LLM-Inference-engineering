"""
PURPOSE:
--------
Producer–Consumer problem using Queue with multiple threads.

ADDED FEATURE:
--------------
Each thread now has a NAME so we can clearly see:
- which Producer is producing
- which Consumer is consuming

BEHAVIOR:
---------
- Producers generate numbers and put them in Queue
- Consumers take numbers from Queue
- Output shows thread identity for clarity
"""

from threading import Thread
from queue import Queue
import time
import random

queue = Queue()
count = 5


# ---------------- PRODUCER ----------------
class Producer(Thread):
    def __init__(self, name, count):
        Thread.__init__(self)
        self.name = name
        self.count = count

    def request(self):
        time.sleep(1)
        return random.randint(0, 100)

    def run(self):
        global queue

        for i in range(self.count):

            value = self.request()

            # Show which producer produced the value
            print(f"[🟢 {self.name}] produced: {value}")

            queue.put(value)


# ---------------- CONSUMER ----------------
class Consumer(Thread):
    def __init__(self, name, count):
        Thread.__init__(self)
        self.name = name
        self.count = count

    def run(self):
        global queue

        for i in range(self.count):

            value = queue.get()

            # Show which consumer consumed the value
            print(f"[🔵 {self.name}] consumed: {value}")

            queue.task_done()


# ---------------- CREATE THREADS ----------------
t1 = Producer("Producer-1", count)
t2 = Producer("Producer-2", count)

t3 = Consumer("Consumer-1", count)
t4 = Consumer("Consumer-2", count)


# ---------------- START THREADS ----------------
t1.start()
t2.start()
t3.start()
t4.start()


# ---------------- WAIT FOR COMPLETION ----------------
t1.join()
t2.join()
t3.join()
t4.join()