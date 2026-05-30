# =========================================================
# FIXED SIZE PROCESS POOL EXAMPLE
# =========================================================
#
# PURPOSE:
# --------
# Demonstrates how a fixed number of worker processes
# can execute many tasks.
#
# Here:
# -----
# - Total Tasks    = 12
# - Worker Processes = 4
#
# The same workers are reused repeatedly.
#
# =========================================================

import multiprocessing
import time


# =========================================================
# TASK FUNCTION
# =========================================================
#
# PURPOSE:
# --------
# Represents a task executed by worker processes.
#
# PARAMETER:
# ----------
# i --> task number
#
# BEHAVIOR:
# ---------
# 1. Gets current worker process
# 2. Prints task start
# 3. Waits 2 seconds
# 4. Prints task completion
#
# =========================================================
def function(i):

    # Get current worker process
    process = multiprocessing.current_process()

    # Display task start
    print(f"start Task {i} (PID:{process.pid})")

    # Simulate processing time
    time.sleep(2)

    # Display task completion
    print(f"end Task {i} (PID:{process.pid})")


# =========================================================
# MAIN PROGRAM
# =========================================================
if __name__ == '__main__':

    # =====================================================
    # CREATE PROCESS POOL WITH 4 WORKERS
    # =====================================================
    #
    # PURPOSE:
    # --------
    # Creates only 4 worker processes.
    #
    # These workers will repeatedly execute tasks.
    #
    # =====================================================
    pool = multiprocessing.Pool(processes=4)

    # Show number of workers
    print(f"Processes started: {pool._processes}")

    # =====================================================
    # EXECUTE 12 TASKS
    # =====================================================
    #
    # Since only 4 workers exist:
    #
    # Workers will execute tasks repeatedly.
    #
    # Example:
    # Worker A -> Task 0 -> Task 4 -> Task 8
    #
    # =====================================================
    for i in range(12):

        # Assign task to process pool
        pool.apply(function, args=(i,))

    # Prevent new tasks
    pool.close()

    # Wait for completion
    pool.join()

    print("END Program")