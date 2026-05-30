"""Multiprocessing PID identification example.

Purpose:
 - Demonstrate how to retrieve the Process ID (PID) of child processes.
 - Show dynamic process creation using a loop and a list for management.

Behavior:
 - The script spawns 5 child processes.
 - Each child process uses `os.getpid()` to identify itself.
 - The parent process (main) manages these children in a list, starts them,
   and ensures they all complete using `join()`.
"""

import multiprocessing
import os
import time


def function():
    """Worker function that identifies its own OS Process ID (PID)."""
    # os.getpid() returns the process ID assigned by the operating system
    pid = os.getpid()
    print("start Process %s" % pid)
    
    # Simulate some work
    time.sleep(2)
    
    print("end Process %s" % pid)
    return


if __name__ == '__main__':
    # List to keep track of process objects
    processes = []
    n_procs = 5

    # 1. Create and start processes in a loop
    for i in range(n_procs):
        p = multiprocessing.Process(target=function)
        processes.append(p)
        p.start()  # Launch the child process

    # 2. Synchronize: wait for all processes to finish
    # Without join(), the main program might exit before the children finish
    for p in processes:
        p.join()

    print("END Program")