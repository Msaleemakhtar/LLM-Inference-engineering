# ============================================================
#        PRODUCER-CONSUMER USING SEMAPHORE(1)
# ============================================================
#
# PURPOSE OF THIS PROGRAM
# ------------------------------------------------------------
#
# This program demonstrates:
#
#   1. Multithreading
#   2. Producer-Consumer model
#   3. Synchronization using Semaphore
#   4. Thread ordering problems
#
# ------------------------------------------------------------
# WHAT IS A SEMAPHORE?
# ------------------------------------------------------------
#
# A Semaphore is a synchronization mechanism used to control
# access to shared resources between multiple threads.
#
# It works using an INTERNAL COUNTER.
#
# Example:
#
#   Semaphore(1)
#
# means:
#
#   One permission is available initially.
#
# So:
#
#   One thread can continue immediately.
#
# ------------------------------------------------------------
# WHAT DOES Semaphore(1) MEAN HERE?
# ------------------------------------------------------------
#
# Initial semaphore counter:
#
#   counter = 1
#
# Therefore:
#
#   The FIRST thread calling acquire()
#   will NOT block.
#
# ------------------------------------------------------------
# IMPORTANT BEHAVIOR OF THIS PROGRAM
# ------------------------------------------------------------
#
# Consumer starts with:
#
#   semaphore.acquire()
#
# Since counter = 1:
#
#   counter becomes:
#
#       1 → 0
#
# Consumer enters immediately.
#
# So Consumer consumes FIRST,
# before Producer creates any data.
#
# Therefore:
#
#   Consumer reads initial value:
#
#       shared = 1
#
# This is NOT ideal Producer-Consumer behavior.
#
# ------------------------------------------------------------
# AFTER FIRST ITERATION
# ------------------------------------------------------------
#
# Consumer next acquire():
#
#   counter = 0
#
# So Consumer BLOCKS and waits.
#
# Producer then produces data and calls:
#
#   semaphore.release()
#
# counter:
#
#   0 → 1
#
# Consumer wakes and consumes produced value.
#
# ------------------------------------------------------------
# PROBLEM IN THIS DESIGN
# ------------------------------------------------------------
#
# First consumed value:
#
#   1 (default value)
#
# Last produced value:
#
#   never consumed
#
# because Consumer already finished all iterations.
#
# ------------------------------------------------------------
# SAMPLE EXECUTION
# ------------------------------------------------------------
#
# consumer has used this: 1
# producer has loaded this: 0
# consumer has used this: 0
# producer has loaded this: 47
# consumer has used this: 47
#
# ------------------------------------------------------------
# IMPORTANT LEARNING
# ------------------------------------------------------------
#
# Semaphore provides synchronization,
# BUT synchronization order must also be correct.
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
#   One thread may continue immediately
#
# ============================================================

semaphore = Semaphore(1)

# Shared resource
shared = 1

# Number of iterations
count = 5


# ============================================================
# REQUEST FUNCTION
# ============================================================
#
# Simulates fetching data from external source
#
# ============================================================

def request():

    # simulate delay
    time.sleep(1)

    # generate random value
    return random.randint(0, 100)


# ============================================================
# CONSUMER THREAD
# ============================================================
#
# Consumer:
#   - waits for semaphore permission
#   - reads shared value
#   - resets shared value to 0
#
# ============================================================

class consumer(Thread):

    def __init__(self, count):

        Thread.__init__(self)

        self.count = count

    def run(self):

        global shared

        for i in range(self.count):

            # ------------------------------------------------
            # acquire()
            #
            # decreases semaphore counter
            #
            # If counter becomes negative:
            #   thread blocks
            # ------------------------------------------------

            semaphore.acquire()

            # ---------------- CRITICAL SECTION ---------------

            print(f"[Consumer] Iteration {i}")
            print(f"consumer has used this: {shared}")

            # Consumer resets shared resource
            shared = 0


# ============================================================
# PRODUCER THREAD
# ============================================================
#
# Producer:
#   - generates random values
#   - stores them in shared variable
#   - releases semaphore to wake Consumer
#
# ============================================================

class producer(Thread):

    def __init__(self, count):

        Thread.__init__(self)

        self.count = count

    def run(self):

        global shared

        for i in range(self.count):

            # Produce new data
            shared = request()

            print(f"[Producer] Iteration {i}")
            print(f"producer has loaded this: {shared}")

            # ------------------------------------------------
            # release()
            #
            # increases semaphore counter
            #
            # wakes waiting Consumer
            # ------------------------------------------------

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

print("\n===================================")
print("Final shared value =", shared)
print("===================================")