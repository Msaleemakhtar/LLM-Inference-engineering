# ============================================================
#            PRODUCER-CONSUMER USING SEMAPHORE
# ============================================================
#
# PURPOSE OF THIS PROGRAM
# ------------------------------------------------------------
#
# This program demonstrates:
#
#   1. Multithreading
#   2. Synchronization using Semaphore
#   3. Shared resource protection
#   4. Producer-Consumer model
#   5. Context manager usage with "with semaphore:"
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
#   Only ONE thread may access the shared resource at a time.
#
# ------------------------------------------------------------
# HOW SEMAPHORE WORKS
# ------------------------------------------------------------
#
# acquire():
#   - decreases internal counter by 1
#   - if no permits available → thread waits
#
# release():
#   - increases internal counter by 1
#   - wakes waiting thread
#
# ------------------------------------------------------------
# WHY COUNTER DECREASES
# ------------------------------------------------------------
#
# Because a thread is USING one available permission.
#
# Example:
#
#   Semaphore(2)
#
# Initial:
#   counter = 2
#
# Thread A enters:
#   counter = 1
#
# Thread B enters:
#   counter = 0
#
# Thread C tries:
#   counter = -1 → blocked/waiting
#
# ------------------------------------------------------------
# PRODUCER-CONSUMER MODEL
# ------------------------------------------------------------
#
# Producer:
#   generates data and stores it
#
# Consumer:
#   reads/uses data
#
# Both access SAME shared variable.
#
# Semaphore prevents both threads from modifying the
# shared variable simultaneously.
#
# ------------------------------------------------------------
# IMPORTANT: "with semaphore:"
# ------------------------------------------------------------
#
# Instead of writing:
#
#   semaphore.acquire()
#   ...
#   semaphore.release()
#
# we can write:
#
#   with semaphore:
#       ...
#
# Python automatically:
#
#   - calls acquire() at beginning
#   - calls release() at end
#
# This is safer and cleaner.
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
#   only 1 thread allowed inside critical section
#
# ============================================================

semaphore = Semaphore(1)

# Shared variable accessed by both threads
shared = 1


# ============================================================
# CONSUMER THREAD
# ============================================================
#
# Consumer:
#   - reads shared data
#   - consumes it
#   - resets value to 0
#
# ============================================================

class Consumer(Thread):

    def __init__(self):

        # Initialize parent Thread class
        Thread.__init__(self)

    def run(self):

        global shared

        # ----------------------------------------------------
        # with semaphore:
        #
        # Automatically does:
        #
        #   semaphore.acquire()
        #   ...
        #   semaphore.release()
        #
        # ----------------------------------------------------

        with semaphore:

            # CRITICAL SECTION
            # Only one thread allowed here

            print("Consumer used value:", shared)

            # Consumer "uses" the data
            shared = 0


# ============================================================
# PRODUCER THREAD
# ============================================================
#
# Producer:
#   - creates new data
#   - stores it into shared variable
#
# ============================================================

class Producer(Thread):

    def __init__(self):

        Thread.__init__(self)

    # --------------------------------------------------------
    # Simulates getting data from external source
    # --------------------------------------------------------

    def request(self):

        # simulate delay
        time.sleep(1)

        # generate random number
        return random.randint(0, 100)

    def run(self):

        global shared

        # Enter critical section safely
        with semaphore:

            # Producer generates new value
            shared = self.request()

            print("Producer loaded value:", shared)


# ============================================================
# CREATE THREADS
# ============================================================

t1 = Producer()
t2 = Consumer()

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

print("\nFinal shared value =", shared)