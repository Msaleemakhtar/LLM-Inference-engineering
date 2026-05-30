"""Demonstrate thread synchronization using a lock.

This example creates two worker threads that both update a shared variable.
Thread A adds to the shared variable while Thread B subtracts from it.
A threading.Lock is used to ensure only one thread enters the critical
section at a time, preventing race conditions and keeping shared state
consistent.
"""

import threading  # Import the threading module to create and manage threads.
import time  # Import the time module to add delays and simulate work.

shared = 0  # Shared global variable accessed by both threads.
lock = threading.Lock()  # Lock object used to protect shared_data access.


def funcA():
    # Thread A increments the shared value in a thread-safe way.
    global shared  # Indicate that this function modifies the module-level shared variable.

    for i in range(10):
        # Acquire the lock before entering the critical section.
        lock.acquire()
        try:
            # Read the current shared value into a local variable.
            local = shared
            # Modify the local copy by adding 10.
            local += 10
            # Sleep to simulate a delay and allow other threads to run.
            time.sleep(1)
            # Write the updated local value back to the shared variable.
            shared = local
            # Print the updated shared value for debugging and traceability.
            print("Thread A wrote: %s" % shared)
        finally:
            # Always release the lock even if an error occurs.
            lock.release()


def funcB():
    # Thread B decrements the shared value in a thread-safe way.
    global shared  # Indicate that this function modifies the module-level shared variable.

    for i in range(10):
        # Acquire the lock before entering the critical section.
        lock.acquire()
        try:
            # Read the current shared value into a local variable.
            local = shared
            # Modify the local copy by subtracting 10.
            local -= 10
            # Sleep to simulate a delay and allow other threads to run.
            time.sleep(1)
            # Write the updated local value back to the shared variable.
            shared = local
            # Print the updated shared value for debugging and traceability.
            print("Thread B wrote: %s" % shared)
        finally:
            # Always release the lock even if an error occurs.
            lock.release()


# Create thread objects for each worker function.
t1 = threading.Thread(target=funcA)
# Thread A will execute funcA.
t2 = threading.Thread(target=funcB)
# Thread B will execute funcB.

# Start both threads so they run concurrently.
t1.start()
t2.start()

# Wait for both threads to finish before exiting the program.
t1.join()
t2.join()
