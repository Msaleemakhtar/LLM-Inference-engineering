"""
PURPOSE:
--------
This program demonstrates thread synchronization using Event.

BEHAVIOR:
---------
1. Producer generates a random number.
2. Consumer waits until Producer signals that data is ready.
3. Event acts as a communication flag between threads.
4. Consumer processes data only after signal is received.

KEY IDEA:
---------
- event.set()   → Producer signals "data is ready"
- event.wait()  → Consumer waits for signal
- event.clear() → Consumer resets signal for next cycle
"""

from threading import Thread, Event
import time
import random

# Event object used for synchronization (initially False)
event = Event()

# Shared resource between threads
shared = 1

# Number of iterations
count = 5


class Consumer(Thread):
    def __init__(self, count):
        Thread.__init__(self)
        self.count = count

    def run(self):
        global shared

        for i in range(self.count):

            # Wait until Producer signals that data is ready
            event.wait()

            # Consume the shared data
            print(f"Consumer has used this: {shared}")

            # Reset shared data (optional logic)
            shared = 0

            # Reset event so Producer can produce next item
            event.clear()


class Producer(Thread):
    def __init__(self, count):
        Thread.__init__(self)
        self.count = count

    def request(self):
        """Simulate time-consuming production task"""
        time.sleep(1)
        return random.randint(0, 100)

    def run(self):
        global shared

        for i in range(self.count):

            # Produce data
            shared = self.request()
            print(f"Producer has loaded this: {shared}")

            # Signal Consumer that data is ready
            event.set()


# Create threads
t1 = Producer(count)
t2 = Consumer(count)

# Start execution
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()