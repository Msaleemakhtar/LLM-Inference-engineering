"""Simple multiprocessing example.

Purpose:
 - Demonstrate basic creation and coordination of multiple
   ``multiprocessing.Process`` instances using an explicit,
   minimal structure (separate ``p1``..``p5`` variables).

Behavior:
 - Each child process runs ``function(i)``, prints a start and end
   message, sleeps for a short time to simulate work, and returns.
 - The main process starts all child processes and waits for them
   to finish using ``join()``.
"""

import multiprocessing
import time


def function(i):
    """Worker function run in a separate process.

    Args:
        i: Identifier for the worker (int).
    """
    # Announce start, simulate work, announce end
    print("start Process %i" % i)
    time.sleep(2)
    print("end Process %i" % i)
    return


if __name__ == "__main__":
    # Create explicit Process objects (keeps original structure)
    p1 = multiprocessing.Process(target=function, args=(1,))
    p2 = multiprocessing.Process(target=function, args=(2,))
    p3 = multiprocessing.Process(target=function, args=(3,))
    p4 = multiprocessing.Process(target=function, args=(4,))
    p5 = multiprocessing.Process(target=function, args=(5,))

    # Start all processes
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

    # Wait for each process to finish
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()

    print("END Program")