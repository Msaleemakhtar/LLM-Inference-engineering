# ============================================================
#                 RLOCK (REENTRANT LOCK) EXAMPLE
# ============================================================
#
# This program demonstrates:
#
#   1. Multiple threads
#   2. Shared variable access
#   3. Synchronization using RLock
#   4. Nested acquire() calls
#
# ------------------------------------------------------------
# WHAT IS RLOCK?
# ------------------------------------------------------------
#
# RLock = Reentrant Lock
#
# A normal Lock allows:
#
#       acquire() -> release()
#
# only once.
#
# If the SAME thread tries:
#
#       lock.acquire()
#       lock.acquire()
#
# it DEADLOCKS itself.
#
# ------------------------------------------------------------
# RLock solves this problem.
# ------------------------------------------------------------
#
# Same thread can acquire the lock multiple times.
#
# Example:
#
#       rlock.acquire()
#       rlock.acquire()
#       rlock.acquire()
#
# This is allowed.
#
# BUT:
#
# The thread must also release it same number of times:
#
#       rlock.release()
#       rlock.release()
#       rlock.release()
#
# Only then the lock becomes free.
#
# ------------------------------------------------------------
# INTERNAL WORKING OF RLOCK
# ------------------------------------------------------------
#
# RLock internally stores:
#
#   1. Owner thread
#   2. Acquire counter
#
# Example:
#
# Thread A:
#
#       acquire() -> counter = 1
#       acquire() -> counter = 2
#
# release():
#
#       counter = 1
#
# Lock STILL belongs to A.
#
# Final release():
#
#       counter = 0
#
# Now another thread may enter.
#
# ------------------------------------------------------------
# THIS PROGRAM
# ------------------------------------------------------------
#
# We create 3 threads:
#
#       A
#       B
#       C
#
# Each thread:
#
#   - acquires outer lock
#   - reads shared variable
#   - acquires inner lock again
#   - modifies shared variable
#   - releases inner lock
#   - releases outer lock
#
# This demonstrates nested locking.
#
# ============================================================

import threading
import time

# Shared variable used by all threads
shared = 0

# Create Reentrant Lock
rlock = threading.RLock()


# ============================================================
# THREAD FUNCTION
# ============================================================
#
# name = thread name
# t    = sleep time
#
# ============================================================

def func(name, t):

    global shared

    # Outer loop runs 3 times
    for i in range(3):

        print(f"\n[{name}] OUTER acquire()")

        # ----------------------------------------------------
        # OUTER acquire()
        # ----------------------------------------------------
        #
        # Thread enters critical section
        #
        # Other threads must wait
        #
        # ----------------------------------------------------

        rlock.acquire()

        print(f"[{name}] OUTER lock acquired")

        # Copy shared value into local variable
        local = shared

        print(f"[{name}] Read shared = {local}")

        # Sleep to simulate long operation
        time.sleep(t)

        # ----------------------------------------------------
        # INNER LOOP
        # ----------------------------------------------------

        for j in range(2):

            print(f"[{name}] INNER acquire()")

            # ------------------------------------------------
            # INNER acquire()
            # ------------------------------------------------
            #
            # SAME THREAD acquires lock AGAIN.
            #
            # Normal Lock would deadlock here.
            #
            # RLock allows it.
            #
            # ------------------------------------------------

            rlock.acquire()

            print(f"[{name}] INNER lock acquired")

            # Modify local variable
            local += 1

            print(f"[{name}] local incremented -> {local}")

            # Sleep again
            time.sleep(2)

            # Update shared variable
            shared = local

            print(f"[{name}] INNER LOOP j={j} wrote shared = {shared}")

            # ------------------------------------------------
            # INNER release()
            # ------------------------------------------------
            #
            # Decreases internal counter
            #
            # Lock STILL belongs to same thread
            # because OUTER lock still active
            #
            # ------------------------------------------------

            rlock.release()

            print(f"[{name}] INNER lock released")

        # ----------------------------------------------------
        # Extra update after inner loop
        # ----------------------------------------------------

        shared = local + 1

        print(f"[{name}] FINAL write shared = {shared}")

        # ----------------------------------------------------
        # OUTER release()
        # ----------------------------------------------------
        #
        # Final release
        #
        # Counter becomes zero
        #
        # Lock finally becomes free
        #
        # Another thread may now enter
        #
        # ----------------------------------------------------

        rlock.release()

        print(f"[{name}] OUTER lock released")


# ============================================================
# CREATE THREADS
# ============================================================

t1 = threading.Thread(target=func, args=('A', 2,))
t2 = threading.Thread(target=func, args=('B', 10,))
t3 = threading.Thread(target=func, args=('C', 1,))


# ============================================================
# START THREADS
# ============================================================

t1.start()
t2.start()
t3.start()


# ============================================================
# WAIT FOR THREADS TO FINISH
# ============================================================

t1.join()
t2.join()
t3.join()


# ============================================================
# FINAL RESULT
# ============================================================

print("\n================================================")
print("Final shared value =", shared)
print("================================================")