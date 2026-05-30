"""Demonstrate thread synchronization with a locking mechanism with context manager.

This example starts two concurrent worker threads that both modify a
shared counter. Thread A adds 10 and Thread B subtracts 10 repeatedly.
A `threading.Lock` is used as a context manager with `with lock:` so only
one thread can update the shared variable at a time, preventing data
corruption from simultaneous access.
"""

import threading  # Import threading to create and manage threads.
import time  # Import time to pause execution and simulate work.

shared_data = 0  # Shared global variable accessed and modified by both threads.
lock = threading.Lock()  # Lock used to ensure exclusive access to shared_data.


def funcA():
    # Thread A increments the shared value in a thread-safe block.
    global shared_data  # Declare shared_data as global so assignments modify the module variable.

    for i in range(10):
        # Acquire the lock before modifying shared_data.
        with lock:
            # Read the shared value into a local variable.
            local = shared_data
            # Increase the local copy by 10.
            local += 10
            # Sleep briefly to simulate work and allow other threads to run.
            time.sleep(1)
            # Write the updated value back to the shared variable.
            shared_data = local
            # Print the current shared_data value to show the update.
            print("Thread A wrote: %s" % shared_data)


def funcB():
    # Thread B decrements the shared value in a thread-safe block.
    global shared_data  # Declare shared_data as global so assignments modify the module variable.

    for i in range(10):
        # Acquire the lock before modifying shared_data.
        with lock:
            # Read the shared value into a local variable.
            local = shared_data
            # Decrease the local copy by 10.
            local -= 10
            # Sleep briefly to simulate work and allow other threads to run.
            time.sleep(1)
            # Write the updated value back to the shared variable.
            shared_data = local
            # Print the current shared_data value to show the update.
            print("Thread B wrote: %s" % shared_data)


# Create two threads, one for funcA and one for funcB.
t1 = threading.Thread(target=funcA)
t2 = threading.Thread(target=funcB)

# Start both threads so they run concurrently.
t1.start()
t2.start()

# Wait for both threads to finish before exiting the program.
t1.join()
t2.join()
