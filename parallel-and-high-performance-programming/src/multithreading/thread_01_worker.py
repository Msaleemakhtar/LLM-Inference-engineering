import threading
import time

# The worker function is executed by each thread instance.
# It prints a start/finish message and sleeps for a short time
# to simulate a long-running task.
def worker(i):
    """Perform work for a single thread.

    Args:
        i (int): Identifier used to distinguish thread output.
    """
    print(f"Worker thread {i} is starting.")
    time.sleep(5)
    print(f"Worker thread {i} is finishing.")


def run_threads():
    """Create and run worker threads, waiting for all to complete."""
    # Build a list of thread objects. Each thread will run the same
    # worker function with a different identifier.
    threads = [
        threading.Thread(target=worker, args=(i,))
        for i in range(1, 6)
    ]

    # Start each thread so they run concurrently.
    for thread in threads:
        thread.start()

    # Wait for every thread to finish before continuing.
    # This ensures the program does not exit early.
    for thread in threads:
        thread.join()

    print("End Program")


if __name__ == "__main__":
    # Allow this module to be run directly for quick testing.
    run_threads()
