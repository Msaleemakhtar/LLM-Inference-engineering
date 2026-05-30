"""Run the threading example.

This helper script invokes the main threading example logic from
`thread_01_worker.py` so the example can be run directly.
"""

from .thread_01_worker import run_threads


def main() -> None:
    run_threads()


if __name__ == "__main__":
    main()
