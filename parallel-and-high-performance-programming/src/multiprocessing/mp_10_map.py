"""
==================== MULTIPROCESSING POOL - DESCRIPTION ====================

👉 PURPOSE:
This program demonstrates how to use a Pool of worker processes to
execute a function on multiple inputs in parallel.

👉 WHAT IS A POOL?
A Pool creates multiple worker processes and distributes tasks among them.

👉 HOW IT WORKS:
1. A Pool of processes is created.
2. The function 'func' is applied to each element of data.
3. Each process works independently (parallel execution).
4. Results are collected and returned in the SAME ORDER as input.

👉 IMPORTANT POINTS:
✔ Parallel execution (faster for heavy tasks)
✔ Uses multiple CPU cores
✔ pool.map() keeps output order same as input
✔ Each task runs in a separate process

👉 REAL-LIFE EXAMPLE:
Think of a Pool as a team of workers:
- Each worker solves a task
- Tasks are done simultaneously
- Results are collected at the end

==============================================================================
"""

import time
import math
import numpy as np
from multiprocessing.pool import Pool


# ==================== FUNCTION TO EXECUTE ====================
def func(value):
    """
    This function will run in separate processes.

    Steps:
    1. Calculate square root of the value
    2. Print result
    3. Sleep for 'value' seconds (to simulate workload)
    4. Return result
    """

    result = math.sqrt(value)

    print("Processing value:", value, "| Result:", result)

    # Simulate heavy computation
    time.sleep(value)

    return result


# ==================== MAIN PROGRAM ====================
if __name__ == "__main__":

    print("Main process started...\n")

    # 🔹 Create Pool of worker processes
    # By default, number of workers = number of CPU cores
    with Pool() as pool:

        # 🔹 Input data (tasks)
        data = np.array([10, 3, 6, 1])

        print("Tasks submitted:", data, "\n")

        # 🔹 Distribute tasks to pool workers
        # Each value goes to a separate process
        results = pool.map(func, data)

        print("\nMain process is going on...")

        # 🔹 Display results (same order as input)
        for result in results:
            print("Final result:", result)

    print("\nEND Program")