"""
==================== PROCESSPOOLEXECUTOR ====================

👉 PURPOSE:
This program demonstrates parallel processing using ProcessPoolExecutor
from the concurrent.futures module.

👉 WHAT IS ProcessPoolExecutor?
- It is a high-level interface for running functions in parallel
- It uses multiple processes (CPU cores)
- It internally manages a pool of worker processes

👉 HOW IT WORKS:
1. A pool of worker processes is created
2. A function is applied to each element of input data
3. Tasks run in parallel (asynchronous execution)
4. Results are collected in order

👉 CONTEXT MANAGER (with statement):
- Automatically manages resources
- Automatically calls shutdown() at the end

👉 CHUNKSIZE:
- Groups multiple tasks together before sending to workers
- Improves performance by reducing overhead

👉 REAL-LIFE EXAMPLE:
Like a factory:
- Each worker process is a machine
- Each machine processes multiple items in batches

=============================================================
"""

import time
import math
import os
import numpy as np
from concurrent.futures import ProcessPoolExecutor


# ==================== FUNCTION EXECUTED BY WORKERS ====================
def func(value):
    """
    This function runs in separate processes.

    Steps:
    1. Compute square root
    2. Get Process ID (PID)
    3. Print processing info
    4. Simulate delay
    5. Return result
    """

    result = math.sqrt(value)

    # 🔹 Get process ID to show which worker is running
    pid = os.getpid()

    print("[PID:%s] Processing value: %s | Result: %s" % (pid, value, result))

    # 🔹 Simulate heavy computation
    time.sleep(value)

    return result


# ==================== MAIN PROGRAM ====================
if __name__ == "__main__":

    print("Main process started...\n")

    # 🔹 Create Process Pool Executor with 10 workers
    with ProcessPoolExecutor(max_workers=4) as executor:

        # 🔹 Input data (tasks)
        data = np.array([10, 3, 6, 1, 4, 5, 2, 9, 7, 3, 4, 6])

        print("Tasks submitted:", data, "\n")

        # 🔹 Submit tasks with chunksize = 4
        results = executor.map(func, data, chunksize=4)

        print("\nMain process is going on...\n")

        # 🔹 Collect results
        for result in results:
            print("Final result:", result)

    print("\nEND Program")