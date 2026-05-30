# =========================================================
# PARALLEL PROCESS POOL USING pool.map()
# =========================================================
#
# PURPOSE:
# --------
# This program demonstrates TRUE parallel execution
# using multiprocessing.Pool and map().
#
# Unlike pool.apply(), which executes tasks sequentially,
# pool.map() distributes tasks among multiple worker
# processes simultaneously.
#
# =========================================================

# Import multiprocessing module
# Used for creating multiple processes
import multiprocessing

# Import time module
# Used here to simulate a long-running task
import time


# =========================================================
# TASK FUNCTION
# =========================================================
#
# PURPOSE:
# --------
# Represents the work each process will perform.
#
# PARAMETER:
# ----------
# i --> Task number
#
# BEHAVIOR:
# ---------
# 1. Gets current worker process
# 2. Prints task start
# 3. Sleeps for 2 seconds
# 4. Prints task completion
#
# =========================================================
def function(i):

    # Get current running worker process
    process = multiprocessing.current_process()

    # Print task start with Process ID
    print(f"Start Task {i} (PID:{process.pid})")

    # Simulate heavy computation
    time.sleep(2)

    # Print task completion
    print(f"End Task {i} (PID:{process.pid})")


# =========================================================
# MAIN PROGRAM
# =========================================================
#
# PURPOSE:
# --------
# Prevents recursive process creation.
#
# This is mandatory in multiprocessing,
# especially on Windows systems.
#
# =========================================================
if __name__ == '__main__':

    # =====================================================
    # CREATE PROCESS POOL
    # =====================================================
    #
    # PURPOSE:
    # --------
    # Creates a pool containing 4 worker processes.
    #
    # These workers will execute tasks in parallel.
    #
    # =====================================================
    pool = multiprocessing.Pool(processes=4)

    # Display total worker processes
    print(f"Processes started: {pool._processes}")

    # =====================================================
    # EXECUTE TASKS IN PARALLEL
    # =====================================================
    #
    # PURPOSE:
    # --------
    # pool.map() distributes tasks automatically
    # among available workers.
    #
    # BEHAVIOR:
    # ---------
    # - Multiple tasks run simultaneously
    # - Workers are reused efficiently
    # - Faster than apply()
    #
    # TASK DISTRIBUTION:
    # ------------------
    # Worker1 -> Task0
    # Worker2 -> Task1
    # Worker3 -> Task2
    # Worker4 -> Task3
    #
    # After completion:
    #
    # Worker1 -> Task4
    # Worker2 -> Task5
    # etc.
    #
    # =====================================================
    pool.map(function, range(12))

    # =====================================================
    # CLOSE POOL
    # =====================================================
    #
    # PURPOSE:
    # --------
    # Prevents new tasks from being submitted.
    #
    # =====================================================
    pool.close()

    # =====================================================
    # WAIT FOR COMPLETION
    # =====================================================
    #
    # PURPOSE:
    # --------
    # Main program waits until all worker
    # processes complete execution.
    #
    # =====================================================
    pool.join()

    # Final message
    print("END PROGRAM")