# ============================================================
#                     SEMAPHORE EXPLAINED
# ============================================================
#
# WHAT IS A SEMAPHORE?
# ------------------------------------------------------------
# A Semaphore is a synchronization tool used in multithreading
# to control access to a shared resource using a COUNTER.
#
# Think of it as a "permission system".
#
# Each thread must take permission (acquire) before entering
# and return permission (release) after leaving.
#
# ------------------------------------------------------------
# WHY COUNTER DECREASES IN acquire()
# ------------------------------------------------------------
#
# Because when a thread enters:
#   → it USES one available permission
#   → so available slots reduce by 1
#
# Example:
#   Semaphore(2)
#
# Initial state:
#   counter = 2  (2 threads allowed)
#
# Thread A calls acquire():
#   counter = 1
#
# Thread B calls acquire():
#   counter = 0
#
# Thread C calls acquire():
#   counter = -1 → BLOCKED (must wait)
#
# IMPORTANT IDEA:
#   counter < 0 means threads are WAITING
#
# ------------------------------------------------------------
# WHY release() INCREASES COUNTER
# ------------------------------------------------------------
#
# Because a thread is leaving the resource:
#   → it frees one permission
#   → so another waiting thread can enter
#
# Example:
#   counter = 0
#
# Thread B calls release():
#   counter = 1
#   → waiting thread C wakes up
#
# ------------------------------------------------------------
# REAL-LIFE ANALOGY (VERY IMPORTANT)
# ------------------------------------------------------------
#
# Imagine a cinema with only 2 seats:
#
# Semaphore(2)
#
# People entering = acquire()
# People leaving  = release()
#
# - 2 people sit (counter becomes 0)
# - 3rd person must wait (counter becomes -1)
#
# ------------------------------------------------------------
# PRODUCER–CONSUMER IDEA
# ------------------------------------------------------------
#
# Producer:
#   creates data
#
# Consumer:
#   uses data
#
# Semaphore ensures:
#   → they do NOT access shared data at the same time
#
# ============================================================

from threading import Thread, Semaphore
import time
import random

# Semaphore initialized with 1 permit
# (acts like a Lock: only 1 thread allowed at a time)
semaphore = Semaphore(1)

# Shared resource between threads
shared = 1


# ============================================================
# CONSUMER THREAD
# ============================================================

class Consumer(Thread):

    def run(self):
        global shared

        # acquire() → take 1 permission
        # counter decreases by 1
        semaphore.acquire()

        # CRITICAL SECTION (safe access)
        print("Consumer read value:", shared)

        # consume data
        shared = 0

        # release() → return permission
        # counter increases by 1
        semaphore.release()


# ============================================================
# PRODUCER THREAD
# ============================================================

class Producer(Thread):

    def request(self):
        time.sleep(1)  # simulate delay
        return random.randint(0, 100)

    def run(self):
        global shared

        # acquire permission (counter -1)
        semaphore.acquire()

        # produce data
        shared = self.request()

        print("Producer generated value:", shared)

        # release permission (counter +1)
        semaphore.release()


# ============================================================
# CREATE THREADS
# ============================================================

t1 = Producer()
t2 = Consumer()

t1.start()
t2.start()

t1.join()
t2.join()

# ============================================================
# FINAL RESULT
# ============================================================

print("\nFinal shared value =", shared)