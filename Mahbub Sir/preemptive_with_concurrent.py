import concurrent.futures
from queue import PriorityQueue

class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.turnaround_time = 0
        self.completion_time = 0
        self.waiting_time = 0

    def run(self, current_time):
        # Wait until the process arrives
        if current_time < self.arrival_time:
            current_time = self.arrival_time

        # Calculate remaining time after executing for 1 time unit
        self.remaining_time -= 1

        # Calculate completion time if the process is complete
        if self.remaining_time == 0:
            self.completion_time = current_time + 1

            # Calculate turnaround time and waiting time
            self.turnaround_time = self.completion_time - self.arrival_time
            self.waiting_time = self.turnaround_time - self.burst_time

        return self.remaining_time

def preemptive_priority_scheduler(processes):
    current_time = 0
    priority_queue = PriorityQueue()
    completed_processes = []

    while processes or not priority_queue.empty():
        while processes and processes[0].arrival_time <= current_time:
            process = processes.pop(0)
            priority_queue.put((process.priority, process))

        if priority_queue.empty():
            current_time += 1
            continue

        _, process = priority_queue.get()

        remaining_time = process.run(current_time)
        current_time += 1

        if remaining_time > 0:
            priority_queue.put((process.priority, process))
        else:
            completed_processes.append(process)

    return completed_processes

if __name__ == "__main__":
    processes_data = [
        (1, 0, 6, 3),
        (2, 2, 4, 1),
        (3, 4, 2, 4),
        (4, 6, 8, 2),
        (5, 8, 10, 5)
    ]

    processes = [Process(pid, arrival_time, burst_time, priority) for pid, arrival_time, burst_time, priority in processes_data]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        completed_processes = preemptive_priority_scheduler(processes)

    total_turnaround_time = 0
    total_waiting_time = 0
    for process in completed_processes:
        total_turnaround_time += process.turnaround_time
        total_waiting_time += process.waiting_time

    num_completed_processes = len(completed_processes)
    average_turnaround_time = total_turnaround_time / num_completed_processes if num_completed_processes > 0 else 0
    average_waiting_time = total_waiting_time / num_completed_processes if num_completed_processes > 0 else 0

    print("Process\tCompletion Time\tTurnaround Time\tWaiting Time")
    for process in completed_processes:
        print(f"{process.pid}\t{process.completion_time}\t\t{process.turnaround_time}\t\t{process.waiting_time}")

    print(f"\nAverage Turnaround Time: {average_turnaround_time}")
    print(f"Average Waiting Time: {average_waiting_time}")
