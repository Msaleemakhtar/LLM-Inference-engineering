"""
==================== PIPE (MULTIPROCESSING) - DESCRIPTION ====================

This program demonstrates inter-process communication using a Pipe in Python.

👉 WHAT IS A PIPE?
A Pipe is a communication channel between TWO processes.
It allows processes to send and receive data.

👉 COMMUNICATION TYPES:
✔ By default:
    receiver, sender = Pipe()
    - One end is mainly used for receiving (recv())
    - Other end is used for sending (send())
    → This behaves like ONE-WAY communication

✔ Duplex mode:
    conn1, conn2 = Pipe(duplex=True)
    - Both ends can send AND receive data
    → This is TWO-WAY communication

👉 HOW IT WORKS:
1. Pipe() creates two connection objects
2. Producer process sends data using send()
3. Consumer process receives data using recv()
4. poll() checks if data is available before receiving

👉 ASYNCHRONOUS BEHAVIOR:
- Both processes run independently
- Producer may send faster or slower than consumer receives
- Only data flow connects them (no direct control)

👉 IMPORTANT POINTS:
✔ Works only between TWO processes
✔ Supports one-way and two-way communication
✔ Data must be picklable
✔ Always close connections after use

👉 REAL-LIFE EXAMPLE:
Pipe is like a phone call:
- One-way → only one person talks
- Two-way → both people talk and listen

==============================================================================
"""

from multiprocessing import Process, Pipe
import time
import random


# ==================== CONSUMER ====================
class Consumer(Process):
    def __init__(self, count, conn):
        super().__init__()
        self.count = count
        self.conn = conn

    def run(self):
        print("Consumer started...\n")

        for i in range(self.count):
            if self.conn.poll():          # check data availability
                item = self.conn.recv()   # receive data
                print("[Consumer] Received:", item)
            else:
                print("[Consumer] Waiting...")

            time.sleep(2)

        print("\nConsumer finished.")


# ==================== PRODUCER ====================
class Producer(Process):
    def __init__(self, count, conn):
        super().__init__()
        self.count = count
        self.conn = conn

    def produce_item(self):
        time.sleep(1)
        return random.randint(1, 100)

    def run(self):
        print("Producer started...\n")

        for i in range(self.count):
            item = self.produce_item()

            self.conn.send(item)   # send data
            print("[Producer] Sent:", item)

        print("\nProducer finished.")


# ==================== MAIN ====================
if __name__ == "__main__":

    print("Main process started...\n")

    receiver, sender = Pipe()   # one-way style usage

    count = 5

    producer = Producer(count, sender)
    consumer = Consumer(count, receiver)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    receiver.close()
    sender.close()

    print("\nMain process finished.")