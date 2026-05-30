# ============================================================
#          PRODUCER-CONSUMER USING SEMAPHORE
# ============================================================
#
# PURPOSE OF THIS PROGRAM
# ------------------------------------------------------------
#
# This program demonstrates:
#
#   1. Multithreading
#   2. Semaphore synchronization
#   3. Shared resource access
#   4. Producer-Consumer model
#   5. Problems in synchronization design
#
# ------------------------------------------------------------
# WHAT IS HAPPENING HERE?
# ------------------------------------------------------------
#
# Producer thread:
#   - generates random values
#   - stores them in shared variable
#
# Consumer thread:
#   - reads values from shared variable
#   - resets shared to 0
#
# Both threads repeat their work 5 times.
#
# ------------------------------------------------------------
# IMPORTANT PROBLEM IN THIS CODE
# ------------------------------------------------------------
#
# Although Semaphore protects the shared variable from
# simultaneous access, the synchronization LOGIC is still wrong.
#
# Why?
#
# Because:
#
#   Producer keeps producing values very quickly
#
# while:
#
#   Consumer may not consume immediately
#
# Result:
#
#   Older produced values get overwritten before consumer
#   reads them.
#
# ------------------------------------------------------------
# EXAMPLE OF BAD BEHAVIOR
# ------------------------------------------------------------
#
# Producer:
#
#   shared = 20
#   shared = 50
#   shared = 90
#   shared = 12
#   shared = 77
#
# Consumer finally runs:
#
#   reads only 77
#
# Previous values:
#
#   20, 50, 90, 12
#
# are LOST forever.
#
# ------------------------------------------------------------
# IMPORTANT CONCEPT
# ------------------------------------------------------------
#
# Semaphore guarantees:
#
#   ✔ safe access
#   ✔ no race condition
#
# BUT it DOES NOT guarantee:
#
#   ✘ correct producer-consumer ordering
#   ✘ no data loss
#
# For correct producer-consumer systems,
# usually Queue objects are used.
#
# ============================================================

from threading import Thread, Semaphore
import time
import random

# ============================================================
# CREATE SEMAPHORE
# ============================================================
#
# Semaphore(1):
#   only ONE thread may access shared variable at a time
#
# ============================================================

semaphore = Semaphore(1)

# Shared resource between threads
shared = 1

# Number of iterations
count = 5


# ============================================================
# CONSUMER THREAD
# ============================================================
#
# Consumer:
#   - reads shared value
#   - consumes it
#   - resets shared to 0
#
# ============================================================

class consumer(Thread):

    def __init__(self, count):

        Thread.__init__(self)

        self.count = count

    def run(self):

        global shared

        # Repeat consume operation multiple times
        for i in range(self.count):

            # ------------------------------------------------
            # acquire() decreases semaphore counter
            #
            # If another thread already inside critical section:
            #       consumer waits
            # ------------------------------------------------

            semaphore.acquire()

            # ---------------- CRITICAL SECTION ---------------

            print(f"[Consumer] Iteration {i}")
            print(f"Consumer used value: {shared}")

            # Consumer resets shared value
            shared = 0

            # ------------------------------------------------
            # release() increases counter
            #
            # allows another waiting thread to continue
            # ------------------------------------------------

            semaphore.release()


# ============================================================
# PRODUCER THREAD
# ============================================================
#
# Producer:
#   - generates random values
#   - stores them in shared variable
#
# ============================================================

class producer(Thread):

    def __init__(self, count):

        Thread.__init__(self)

        self.count = count

    # --------------------------------------------------------
    # Simulates external data request
    # --------------------------------------------------------

    def request(self):

        # simulate delay
        time.sleep(1)

        # generate random number
        return random.randint(0, 100)

    def run(self):

        global shared

        # Repeat production multiple times
        for i in range(self.count):

            # acquire semaphore
            semaphore.acquire()

            # ---------------- CRITICAL SECTION ---------------

            # Producer generates new value
            shared = self.request()

            print(f"[Producer] Iteration {i}")
            print(f"Producer loaded value: {shared}")

            # release semaphore
            semaphore.release()


# ============================================================
# CREATE THREADS
# ============================================================

t1 = producer(count)
t2 = consumer(count)

# ============================================================
# START THREADS
# ============================================================

t1.start()
t2.start()

# ============================================================
# WAIT FOR THREADS TO FINISH
# ============================================================

t1.join()
t2.join()

# ============================================================
# FINAL RESULT
# ============================================================

print("\n====================================")
print("Final shared value =", shared)
print("====================================")