# ============================================================
#        PRODUCER–CONSUMER USING Condition
# ============================================================
#
# PURPOSE
# ------------------------------------------------------------
# This program shows how CONDITION VARIABLES work in threads.
#
# A Condition allows:
#   1. Threads to WAIT until a condition becomes true
#   2. One thread to NOTIFY another thread
#
# It is built on top of a Lock.
#
# ============================================================

# from threading import Thread, Condition
# import time
# import random

# # Condition object (contains internal Lock)
# condition = Condition()

# # Shared resource between Producer and Consumer
# shared = 0

# # Number of cycles
# count = 5


# # ============================================================
# # CONSUMER THREAD
# # ============================================================

# class Consumer(Thread):

#     def __init__(self, count):
#         Thread.__init__(self)
#         self.count = count

#     def run(self):
#         global shared

#         for i in range(self.count):
#             with condition:
#                 # Wait until there is valid data to consume
#                 while shared == 0:
#                     condition.wait()

#                 # Consume the data
#                 print(f"[Consumer] used value: {shared}")

#                 # Mark data as consumed
#                 shared = 0

#                 # Wake producer to produce the next value
#                 condition.notify()


# # ============================================================
# # PRODUCER THREAD
# # ============================================================

# class Producer(Thread):

#     def __init__(self, count):
#         Thread.__init__(self)
#         self.count = count

#     def request(self):
#         # simulate delay
#         time.sleep(1)
#         return random.randint(0, 100)

#     def run(self):
#         global shared

#         for i in range(self.count):
#             value = self.request()

#             with condition:
#                 # Wait until the consumer has consumed the last value
#                 while shared != 0:
#                     condition.wait()

#                 # Produce data
#                 shared = value
#                 print(f"[Producer] loaded value: {shared}")

#                 # Wake consumer that is waiting
#                 condition.notify()


# # ============================================================
# # CREATE THREADS
# # ============================================================

# t1 = Producer(count)
# t2 = Consumer(count)

# # ============================================================
# # START THREADS
# # ============================================================

# t1.start()
# t2.start()

# t1.join()
# t2.join()


# # ============================================================
# # FINAL OUTPUT
# # ============================================================

# print("\nFinal shared value =", shared)


# ============================================================
# ADDITIONAL CODE BLOCK FROM REQUEST
# ============================================================
# The following block is placed below the main example and includes
# inline comments describing the use of Condition, acquire/wait/notify,
# and shared state synchronization.

from threading import Thread, Condition
import time
import random

# Create a Condition object for coordinating threads.
condition = Condition()

# Shared state between producer and consumer.
shared = 1
count = 5

class Consumer(Thread):
    def __init__(self, count):
        Thread.__init__(self)
        global condition
        self.count = count

    def run(self):
        global shared
        for i in range(self.count):
            condition.acquire()

            # If there is no valid data, wait until producer notifies.
            if shared == 0:
                condition.wait()

            print("consumer has used this: %s" % shared)

            # Mark the data as consumed.
            shared = 0

            # Notify the producer that it can generate the next value.
            condition.notify()
            condition.release()

class Producer(Thread):
    def __init__(self, count):
        Thread.__init__(self)
        self.count = count
        global condition

    def request(self):
        time.sleep(1)
        return random.randint(0, 100)

    def run(self):
        global shared
        for i in range(self.count):
            condition.acquire()
            shared = self.request()
            print("producer has loaded this: %s" % shared)

            # This example waits for the consumer to consume before
            # notifying again, illustrating the producer/consumer handoff.
            condition.wait()
            if shared == 0:
                condition.notify()
            condition.release()

t1 = Producer(count)
t2 = Consumer(count)
t1.start()
t2.start()
t1.join()
t2.join()