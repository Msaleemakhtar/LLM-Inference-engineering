"""
==================== MULTIPROCESSING map_async() ====================

👉 PURPOSE:
This program demonstrates asynchronous execution using Pool.map_async()

👉 WHAT IS map_async()?
- It applies a function to all items in parallel (like map)
- BUT it does NOT block the main process
- It immediately returns an AsyncResult object

👉 HOW IT WORKS:
1. Tasks are submitted to worker processes
2. Main process continues execution without waiting
3. Results are collected later using .get()

👉 KEY IDEA:
map_async() = NON-BLOCKING (asynchronous)

=====================================================================
"""

import time
import math
import numpy as np
from multiprocessing.pool import Pool


def func(value):
    result = math.sqrt(value)
    print("Processing:", value, "| Result:", result)

    time.sleep(value)   # simulate work
    return result


if __name__ == "__main__":

    print("Main process started...\n")

    with Pool() as pool:

        data = np.array([10, 3, 6, 1])

        # 🔹 Asynchronous execution
        results = pool.map_async(func, data)

        # 🔹 Main process does NOT wait here
        print("Main Process is going on...\n")

        # 🔹 Now wait and get results
        final_results = results.get()

        for result in final_results:
            print("This is the result:", result)

    print("\nEND Program")