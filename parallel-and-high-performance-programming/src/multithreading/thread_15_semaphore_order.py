# ============================================================
#      PERFECT PRODUCER-CONSUMER SYNCHRONIZATION
#              USING Semaphore(0)
# ============================================================
#
# ============================================================
# VERY IMPORTANT CONCEPT:
# HOW Semaphore(0) GUARANTEES CORRECT ORDER
# ============================================================
#
# We want this execution order:
#
#   Producer produces data
#   → Consumer consumes data
#
# NOT this:
#
#   Consumer consumes BEFORE production
#
# ------------------------------------------------------------
# WHY Semaphore(0) WORKS
# ------------------------------------------------------------
#
# Initial state:
#
#   semaphore = Semaphore(0)
#
# Internal counter:
#
#   counter = 0
#
# Meaning:
#
#   NO thread has permission to continue initially.
#
# ------------------------------------------------------------
# STEP-BY-STEP EXECUTION
# ------------------------------------------------------------
#
# STEP 1:
#
# Consumer starts first and executes:
#
#   semaphore.acquire()
#
# Counter changes:
#
#   0 → -1
#
# Since counter became negative:
#
#   Consumer BLOCKS and waits.
#
# Consumer CANNOT continue further.
#
# ------------------------------------------------------------
# STEP 2:
#
# Producer runs.
#
# Producer generates data:
#
#   shared = request()
#
# Example:
#
#   shared = 25
#
# ------------------------------------------------------------
# STEP 3:
#
# Producer executes:
#
#   semaphore.release()
#
# Counter changes:
#
#   -1 → 0
#
# Waiting Consumer wakes up.
#
# ------------------------------------------------------------
# STEP 4:
#
# Consumer continues execution:
#
#   print(shared)
#
# Consumer now reads:
#
#   25
#
# Correct order achieved:
#
#   Produce → Consume
#
# ------------------------------------------------------------
# IMPORTANT IDEA
# ------------------------------------------------------------
#
# We are NOT depending on:
#
#   ✘ thread speed
#   ✘ CPU timing
#   ✘ operating system scheduling
#   ✘ luck
#
# Instead:
#
#   Semaphore FORCES correct ordering.
#
# ------------------------------------------------------------
# WHAT WOULD HAPPEN WITH Semaphore(1)?
# ------------------------------------------------------------
#
# Initial counter:
#
#   counter = 1
#
# Consumer acquire():
#
#   1 → 0
#
# Consumer continues immediately.
#
# So Consumer consumes BEFORE Producer produces.
#
# That caused the earlier synchronization problem.
#
# ============================================================
# PURPOSE OF THIS PROGRAM
# ============================================================
#
# This program demonstrates:
#
#   1. Multithreading
#   2. Producer-Consumer synchronization
#   3. Correct use of Semaphore
#   4. Thread ordering control
#
# ============================================================

from threading import Thread, Semaphore
import time
import random

# ============================================================
# CREATE SEMAPHORE
# ============================================================

semaphore = Semaphore(0)

# Shared resource
shared = 0

# Number of synchronized cycles
count = 5


# ============================================================
# REQUEST FUNCTION
# ============================================================

def request():

    # simulate external delay
    time.sleep(1)

    # generate random value
    return random.randint(0, 100)


# ============================================================
# CONSUMER THREAD
# ============================================================

class Consumer(Thread):

    def __init__(self, count):

        Thread.__init__(self)

        self.count = count

    def run(self):

        global shared

        for i in range(self.count):

            # ------------------------------------------------
            # acquire()
            #
            # Consumer waits here until Producer
            # gives permission using release()
            # ------------------------------------------------

            semaphore.acquire()

            # ---------------- CRITICAL SECTION ---------------

            print(f"[Consumer] Cycle {i}")
            print(f"Consumer used value: {shared}")

            # reset shared resource
            shared = 0


# ============================================================
# PRODUCER THREAD
# ============================================================

class Producer(Thread):

    def __init__(self, count):

        Thread.__init__(self)

        self.count = count

    def run(self):

        global shared

        for i in range(self.count):

            # produce data
            shared = request()

            print(f"[Producer] Cycle {i}")
            print(f"Producer loaded value: {shared}")

            # ------------------------------------------------
            # release()
            #
            # Gives permission to waiting Consumer
            # ------------------------------------------------

            semaphore.release()


# ============================================================
# CREATE THREADS
# ============================================================

t1 = Producer(count)
t2 = Consumer(count)

# ============================================================
# START THREADS
# ============================================================

# Consumer starts first but immediately blocks
t2.start()

# Producer starts and wakes Consumer
t1.start()

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