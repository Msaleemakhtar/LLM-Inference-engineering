"""
PURPOSE:
--------
This program demonstrates multithreading using Event synchronization
with multiple Producer and Consumer threads.

BEHAVIOR:
---------
1. Two Producer threads generate random numbers.
2. Two Consumer threads wait for the event signal.
3. Producers write data into a shared variable.
4. Consumers read and reset the shared variable.
5. Event is used to signal when data is available.

EXPECTED PROBLEM:
-----------------
Because multiple producers and consumers share one variable:
- Values may be overwritten (lost updates)
- Consumers may read incorrect or reset values (0)
- Event is not sufficient for full synchronization in multi-thread setup
"""

from threading import Thread, Event
import time
import random

# Event object used for signaling between threads
event = Event()

# Shared variable between all threads (not protected)
shared = 1

# Number of iterations each thread will run
count = 5


class Consumer(Thread):
    def __init__(self, count):
        Thread.__init__(self)
        global event
        self.count = count

    def run(self):
        global shared

        for i in range(self.count):

            # Wait until a producer signals that data is ready
            event.wait()

            # Consumer reads shared value
            print("consumer has used this: %s" % shared)

            # Reset shared value (can cause race issues)
            shared = 0

            # Reset event for next cycle
            event.clear()


class Producer(Thread):
    def __init__(self, count):
        Thread.__init__(self)
        self.count = count
        global event

    def request(self):
        # Simulate delay in producing data
        time.sleep(1)
        return random.randint(0, 100)

    def run(self):
        global shared

        for i in range(self.count):

            # Producer generates value
            shared = self.request()

            # Print produced value
            print("producer has loaded this: %s" % shared)

            # Signal consumers that data is ready
            event.set()


# Create two Producer threads
t1 = Producer(count)
t2 = Producer(count)

# Create two Consumer threads
t3 = Consumer(count)
t4 = Consumer(count)

# Start all threads
t1.start()
t2.start()
t3.start()
t4.start()

# Wait for all threads to finish
t1.join()
t2.join()
t3.join()
t4.join()