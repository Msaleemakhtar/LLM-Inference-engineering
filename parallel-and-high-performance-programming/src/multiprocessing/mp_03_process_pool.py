# =========================================================
# PROCESS POOL EXAMPLE USING multiprocessing.Pool
# =========================================================
#
# PURPOSE:
# --------
# This program demonstrates how to use a Process Pool
# in Python for executing tasks using multiple processes.
#
# A Process Pool automatically manages worker processes
# and distributes tasks among them.
#
# =========================================================

# Import multiprocessing module
# Used for creating multiple processes
import multiprocessing

# Import time module
# Used here to simulate a time-consuming task
import time


# =========================================================
# WORKER FUNCTION
# =========================================================
#
# PURPOSE:
# --------
# This function represents the task that each process
# in the pool will execute.
#
# PARAMETER:
# ----------
# i --> task number
#
# BEHAVIOR:
# ---------
# 1. Gets current process information
# 2. Prints start message
# 3. Waits for 2 seconds
# 4. Prints completion message
#
# =========================================================
def function(i):

    # Get currently running process object
    process = multiprocessing.current_process()

    # Print start message with process ID
    print(f"Start Task {i} (PID: {process.pid})")

    # Simulate heavy processing
    time.sleep(2)

    # Print completion message
    print(f"End Task {i} (PID: {process.pid})")


# =========================================================
# MAIN PROGRAM
# =========================================================
#
# PURPOSE:
# --------
# Prevents child processes from recursively executing
# the same code (important in Windows).
#
# =========================================================
if __name__ == '__main__':

    # =====================================================
    # CREATE PROCESS POOL
    # =====================================================
    #
    # PURPOSE:
    # --------
    # Creates a pool of worker processes.
    #
    # By default:
    # Number of workers = Number of CPU cores
    #
    # Example:
    # 4-core CPU --> 4 worker processes
    #
    # =====================================================
    pool = multiprocessing.Pool()

    # Display total number of worker processes
    print(f"Processes started: {pool._processes}")

    # =====================================================
    # EXECUTE TASKS
    # =====================================================
    #
    # PURPOSE:
    # --------
    # Assign tasks to worker processes.
    #
    # pool.apply():
    # -------------
    # Executes one task at a time.
    # It is BLOCKING.
    #
    # BLOCKING means:
    # Next task waits until current task finishes.
    #
    # =====================================================
    for i in range(pool._processes):

        # Execute function(i)
        # args=(i,) passes argument to function
        pool.apply(function, args=(i,))

    # =====================================================
    # CLOSE POOL
    # =====================================================
    #
    # PURPOSE:
    # --------
    # Prevents any more tasks from being added.
    #
    # =====================================================
    pool.close()

    # =====================================================
    # WAIT FOR ALL PROCESSES
    # =====================================================
    #
    # PURPOSE:
    # --------
    # Main program waits until all worker processes finish.
    #
    # =====================================================
    pool.join()

    # Final message
    print("END PROGRAM")