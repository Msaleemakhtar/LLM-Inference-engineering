# ============================================================
#            THREAD SYNCHRONIZATION USING LOCKS
# ============================================================
#
# This example demonstrates an UNUSUAL use of threading.Lock().
#
# Normally:
#
#       acquire() and release()
#
# are used INSIDE THE SAME THREAD.
#
# Example:
#
#       lock.acquire()
#       # critical section
#       lock.release()
#
# This protects shared data from race conditions.
#
# ------------------------------------------------------------
# BUT IN THIS EXAMPLE:
# ------------------------------------------------------------
#
# Thread A acquires the lock
# Thread B releases the lock
#
# So the lock is NOT being used as simple protection.
#
# Instead, it is being used as:
#
#       A SIGNAL / TURN-TAKING MECHANISM
#
# The threads coordinate with each other:
#
#       "Now your turn"
#       "Now my turn"
#
# ------------------------------------------------------------
# IMPORTANT CONCEPT
# ------------------------------------------------------------
#
# The lock has only 2 states:
#
#       UNLOCKED
#       LOCKED
#
# If a thread calls:
#
#       lock.acquire()
#
# while the lock is already LOCKED:
#
#       that thread BLOCKS (WAITS)
#
# until another thread calls:
#
#       lock.release()
#
# ------------------------------------------------------------
# FLOW OF THIS PROGRAM
# ------------------------------------------------------------
#
# 1. Thread B acquires the lock first
#
# 2. Thread B subtracts 10
#
# 3. Thread B releases the lock
#
# 4. Thread A wakes up and acquires the lock
#
# 5. Thread A adds 10
#
# 6. Thread A tries acquire() again
#
# 7. Since lock already locked -> A blocks
#
# 8. Thread B releases again
#
# 9. A wakes again
#
# This creates alternating execution:
#
#       B -> A -> B -> A
#
# ------------------------------------------------------------
# DANGER
# ------------------------------------------------------------
#
# This style is dangerous because:
#
# - acquire() and release() are asymmetric
# - timing dependent
# - can deadlock
# - hard to debug
#
# Normally, locks should be used symmetrically.
#
# ============================================================

import threading
import time

# Shared variable accessed by both threads
shared = 0

# Create lock object
lock = threading.Lock()


# ============================================================
# THREAD A
# ============================================================
#
# This thread:
#
#       + adds 10 to shared variable
#       + then acquires lock
#
# Important:
# It NEVER releases the lock itself.
#
# Thread B will release it.
#
# ============================================================

def funcA():

    global shared

    # Repeat 10 times
    for i in range(10):

        # Sleep to force thread switching
        time.sleep(1)

        # Modify shared variable
        shared += 10

        # Print current value and iteration
        print(f"[A] shared = {shared}, iteration = {i}")

        # ----------------------------------------------------
        # acquire()
        # ----------------------------------------------------
        #
        # If lock is unlocked:
        #       A acquires it and continues
        #
        # If lock is already locked:
        #       A BLOCKS and waits
        #
        # ----------------------------------------------------

        print("[A] Trying to acquire lock...")

        lock.acquire()

        print("[A] Lock acquired")


# ============================================================
# THREAD B
# ============================================================
#
# This thread:
#
#       + acquires lock first
#       + subtracts 10
#       + releases lock repeatedly
#
# Thread B acts like a SIGNALER.
#
# ============================================================

def funcB():

    global shared

    # --------------------------------------------------------
    # First acquire()
    # --------------------------------------------------------
    #
    # B locks the lock initially.
    #
    # This means:
    #       Thread A may later block waiting for B
    #
    # --------------------------------------------------------

    print("[B] Acquiring initial lock...")

    lock.acquire()

    print("[B] Initial lock acquired")

    # Repeat 10 times
    for i in range(10):

        # Sleep to force context switching
        time.sleep(1)

        # Modify shared variable
        shared -= 10

        # Print current value and iteration
        print(f"[B] shared = {shared}, iteration = {i}")

        # ----------------------------------------------------
        # release()
        # ----------------------------------------------------
        #
        # This unlocks the lock.
        #
        # If Thread A is waiting:
        #       Thread A wakes up
        #
        # ----------------------------------------------------

        print("[B] Releasing lock...")

        lock.release()

        print("[B] Lock released")


# ============================================================
# CREATE THREADS
# ============================================================

t1 = threading.Thread(target=funcA)
t2 = threading.Thread(target=funcB)


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