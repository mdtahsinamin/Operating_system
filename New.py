import threading
import time

class MutexLock:
    def __init__(self):
        self.lock = threading.Lock()

    def aquire(self):
        self.lock.acquire()

    def relase(self):
        self.lock.release()



def criticalSection(lock, thread_id):
    lock.aquire()
    print(f"Thread - {thread_id} is in critical section")
    time.sleep(2)
    print(f"Thread {thread_id} is exiting the critical section")
    lock.relase()


def worker(lock, thread_id):
    print(f"Thread - {thread_id} is starting")
    criticalSection(lock, thread_id)
    print(f"Thread - {thread_id} is done")


lock = MutexLock()
threads = []
for i in range(3):
    thread = threading.Thread(target=worker, args=(lock, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
