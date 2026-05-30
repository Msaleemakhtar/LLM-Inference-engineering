from multiprocessing import Process, Queue
import time
import random

# -------------------- Consumer Class --------------------
class Consumer(Process):
    def __init__(self, count, queue):
        super().__init__()
        self.count = count
        self.queue = queue

    def run(self):
        for i in range(self.count):

            # Check if queue is empty before getting data
            if self.queue.empty():
                print("Consumer: Queue is empty, waiting...")
                time.sleep(1)

            # Get item from queue (FIFO)
            item = self.queue.get()

            # Show current queue size
            print("Consumer: got", item, "| Queue size now:", self.queue.qsize())

            # Simulate processing time
            time.sleep(2)


# -------------------- Producer Class --------------------
class Producer(Process):
    def __init__(self, count, queue):
        super().__init__()
        self.count = count
        self.queue = queue

    def produce_item(self):
        time.sleep(1)  # simulate delay
        return random.randint(1, 100)

    def run(self):
        for i in range(self.count):

            item = self.produce_item()

            # Check if queue is full before adding
            if self.queue.full():
                print("Producer: Queue is full, waiting...")
                time.sleep(1)

            # Put item into queue
            self.queue.put(item)

            # Show current queue size
            print("Producer: added", item, "| Queue size now:", self.queue.qsize())


# -------------------- Main Program --------------------
if __name__ == "__main__":

    # Create queue with small size to show full() behavior
    queue = Queue(maxsize=3)

    count = 6   # number of items

    # Create processes
    producer = Producer(count, queue)
    consumer = Consumer(count, queue)

    # Start processes
    producer.start()
    consumer.start()

    # Wait for both to finish
    producer.join()
    consumer.join()

    print("Program finished.")