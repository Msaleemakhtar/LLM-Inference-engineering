"""
==================== MULTIPROCESSING POOL WITH CHUNKSIZE ====================

👉 PURPOSE:
This program demonstrates parallel processing using Pool.map()
with chunksize to improve performance.

👉 WHAT IS POOL?
A Pool creates multiple worker processes that execute tasks in parallel.

👉 WHAT IS map()?
- Applies a function to all elements of a list
- Blocks the main process until all tasks are complete
- Returns results in the SAME order as input

👉 WHAT IS CHUNKSIZE?
- It defines how many tasks are grouped and sent to each worker
- Instead of sending one task at a time, tasks are sent in batches

👉 HOW IT WORKS:
1. Input data is divided into chunks (groups)
2. Each worker process gets one chunk
3. Workers process their chunk sequentially
4. All workers run in parallel
5. Results are collected and returned in order

👉 EXAMPLE:
Data = 12 items, chunksize = 4
→ 3 chunks:
   [10,3,6,1], [4,5,2,9], [7,3,4,6]

👉 IMPORTANT POINTS:
✔ Parallel execution (multiple processes)
✔ chunksize improves efficiency
✔ Output order is maintained
✔ Execution inside workers is asynchronous

👉 REAL-LIFE EXAMPLE:
Workers in a factory:
- Each worker gets a bundle of tasks (chunk)
- All workers work at the same time
- Results are collected at the end

==============================================================================
"""

import time
import math
import numpy as np
from multiprocessing.pool import Pool


# ==================== FUNCTION ====================
def func(value):
    """
    This function runs inside worker processes.

    Steps:
    1. Compute square root
    2. Print value and result
    3. Sleep to simulate workload
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

    # 🔹 Create pool of worker processes
    with Pool() as pool:

        # 🔹 Input data (12 tasks)
        data = np.array([10, 3, 6, 1, 4, 5, 2, 9, 7, 3, 4, 6])

        print("Tasks:", data, "\n")

        # 🔹 Apply function in parallel with chunksize = 4
        results = pool.map(func, data, chunksize=4)

        print("\nMain process is going on...\n")

        # 🔹 Display results (order preserved)
        for result in results:
            print("Final result:", result)

    print("\nEND Program")