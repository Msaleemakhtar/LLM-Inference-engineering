# =========================================================
# PROCESS SUBCLASSING EXAMPLE (multiprocessing.Process)
# =========================================================
#
# PURPOSE:
# --------
# This program demonstrates an alternative way of creating
# parallel processes in Python by subclassing Process.
#
# Instead of using:
#   Process(target=function)
#
# we define:
#   class MyProcess(Process)
#
# and override:
#   - __init__() → to initialize data
#   - run()      → to define task logic
#
# =========================================================

from multiprocessing import Process
import time
import random


# =========================================================
# CUSTOM PROCESS CLASS
# =========================================================
#
# PURPOSE:
# --------
# This class defines a custom worker process.
# Each object of this class runs independently.
#
# =========================================================
class ChildProcess(Process):

    # =====================================================
    # INITIALIZER METHOD
    # =====================================================
    #
    # PURPOSE:
    # --------
    # Used to initialize process-specific data.
    #
    # PARAMETERS:
    # ----------
    # count → task identifier (process number)
    #
    # =====================================================
    def __init__(self, count):

        # Initialize parent Process class
        Process.__init__(self)

        # Store custom data for this process
        self.count = count

    # =====================================================
    # RUN METHOD (MAIN EXECUTION BODY)
    # =====================================================
    #
    # PURPOSE:
    # --------
    # This method contains the code that will be executed
    # when the process starts.
    #
    # IMPORTANT:
    # ----------
    # - This is automatically called when .start() is used
    # - Each process runs independently
    #
    # =====================================================
    def run(self):

        # Print start message
        print(f"Start Process {self.count}")

        # Simulate workload
        time.sleep(2)

        # Print end message
        print(f"End Process {self.count}")


# =========================================================
# MAIN PROGRAM
# =========================================================
#
# PURPOSE:
# --------
# Creates multiple process objects and runs them in parallel.
#
# =========================================================
if __name__ == "__main__":

    # List to store process objects
    processes = []

    # Number of processes to create
    n_procs = 5

    # =====================================================
    # CREATE AND START PROCESSES
    # =====================================================
    #
    # PURPOSE:
    # --------
    # - Create process objects
    # - Start execution immediately
    #
    # =====================================================
    for i in range(n_procs):

        # Create process object
        p = ChildProcess(i)

        # Store in list (for later join)
        processes.append(p)

        # Start process (calls run() internally)
        p.start()

    # =====================================================
    # WAIT FOR ALL PROCESSES TO FINISH
    # =====================================================
    #
    # PURPOSE:
    # --------
    # Ensures main program waits until all processes complete.
    #
    # =====================================================
    for i in range(n_procs):

        processes[i].join()


# =========================================================
# END OF PROGRAM
# =========================================================