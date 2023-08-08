import threading
import time

class PetersonLock:
    def __init__(self):
        self.flag = [False, False]
        self.turn = 0

    def lock(self, process_id):
        other_process_id = 1 - process_id
        self.flag[process_id] = True
        self.turn = process_id
        while self.flag[other_process_id] and self.turn == process_id:
            if process_id == 0:
                print("Producer is waiting...Consumer in Critical Section\n")
            else:
                print("Consumer is waiting...Producer in Critical Section \n")
            pass

    def unlock(self, process_id):
        self.flag[process_id] = False

def producer(lock, buffer, item):
    lock.lock(0)  # Producer's turn 0
    print(f"Producer is in Critical Section - Producing item {item} \n")
    buffer.append(item)
    lock.unlock(0)

def consumer(lock, buffer):
    lock.lock(1)  # Consumer's turn 1
    while not buffer:
        print("Consumer is waiting... buffer empty")
        pass  # Wait if buffer is empty
    item = buffer.pop(0)
    print(f"Consumer is in Critical Section - Consuming item {item} \n")
    lock.unlock(1)

if __name__ == "__main__":
    lock = PetersonLock()
    buffer = []
    for i in range(5):
        producer_thread = threading.Thread(target=producer, args=(lock, buffer, i))
        consumer_thread = threading.Thread(target=consumer, args=(lock, buffer))
        producer_thread.start()
        consumer_thread.start()
        producer_thread.join()
        consumer_thread.join()
