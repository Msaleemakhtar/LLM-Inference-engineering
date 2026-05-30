import threading
import time

# This example demonstrates how to use join() to wait for thread completion.
# Two groups of threads are started separately to show how the main program
# can wait for thread sets before continuing.

def function(i):
    """Simulate work performed by a single thread.

    Args:
        i (int): Thread identifier used for output clarity.
    """
    print(f"start Thread {i}")
    time.sleep(2)
    print(f"end Thread {i}")


# Create five worker thread objects.
t1 = threading.Thread(target=function, args=(1,))
t2 = threading.Thread(target=function, args=(2,))
t3 = threading.Thread(target=function, args=(3,))
t4 = threading.Thread(target=function, args=(4,))
t5 = threading.Thread(target=function, args=(5,))

# Start the first group of threads and wait for them to finish.
# Using join() ensures the main thread does not exit before the workers complete.
t1.start()
t2.start()
t1.join()
t2.join()

print("First set of threads done")
print("The program can execute other code here")

# Start the second group of threads after the first group has finished.
t3.start()
t4.start()
t5.start()

# Wait for the remaining threads to finish before ending the program.
t3.join()
t4.join()
t5.join()

print("Second set of threads done")
print("END Program")
