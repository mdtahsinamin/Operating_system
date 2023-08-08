import threading
import time

class MutexLock:
    def __init__(self):
        self.lock = threading.Lock()

    def acquire(self):
        self.lock.acquire()

    def release(self):
        self.lock.release()

def critical_section(lock, thread_id):
    lock.acquire()
    print(f"Thread {thread_id} is in the critical section")
    time.sleep(2)  # Simulate some work in the critical section
    print(f"Thread {thread_id} is exiting the critical section")
    lock.release()

def worker(lock, thread_id):
    print(f"Thread {thread_id} is starting")
    critical_section(lock, thread_id)
    print(f"Thread {thread_id} is done")

if __name__ == "__main__":
    mutex_lock = MutexLock()
    threads = []
    for i in range(3):
        thread = threading.Thread(target=worker, args=(mutex_lock, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All threads have completed")
