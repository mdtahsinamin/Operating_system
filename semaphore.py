# semaphore is a variable
# buffer limit

# wait -> s--
# signal -> s++

# producer
# consumer
import threading

semaphore = 5
limit = 5

def wait():
    global semaphore, limit

    while semaphore <= 0:
        print("Block or buffer full \n")

    semaphore = semaphore - 1

def signal():
    global  semaphore, limit

    while semaphore >= limit:
        print("Wakeup or buffer empty \n")

    semaphore = semaphore + 1


def producer():
    for i in range(10):
        wait()
        print("Produced \n")


def consumer():
    for i in range(10):
        signal()
        print("Consumed \n")


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()