import concurrent.futures

class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.turnaround_time = 0
        self.completion_time = 0
        self.waiting_time = 0

    def run(self, current_time):
        # Wait until the process arrives
        if current_time < self.arrival_time:
            current_time = self.arrival_time

        # Calculate completion time
        self.completion_time = current_time + self.burst_time

        # Calculate turnaround time and waiting time
        self.turnaround_time = self.completion_time - self.arrival_time
        self.waiting_time = self.turnaround_time - self.burst_time

        return self.completion_time

def sjf_scheduler(processes):
    current_time = 0
    completed_processes = []

    while processes:
        available_processes = [process for process in processes if process.arrival_time <= current_time]
        if not available_processes:
            current_time += 1
            continue

        shortest_process = min(available_processes, key=lambda p: p.burst_time)
        processes.remove(shortest_process)
        completion_time = shortest_process.run(current_time)
        completed_processes.append((shortest_process, completion_time))
        current_time = completion_time

    return completed_processes

if __name__ == "__main__":
    processes_data = [
        (1, 0, 6),
        (2, 2, 4),
        (3, 4, 2),
        (4, 6, 8),
        (5, 8, 10)
    ]

    processes = [Process(pid, arrival_time, burst_time) for pid, arrival_time, burst_time in processes_data]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        completed_processes = sjf_scheduler(processes)

    total_turnaround_time = 0
    total_waiting_time = 0
    for process, _ in completed_processes:
        total_turnaround_time += process.turnaround_time
        total_waiting_time += process.waiting_time

    average_turnaround_time = total_turnaround_time / len(completed_processes)
    average_waiting_time = total_waiting_time / len(completed_processes)

    print("Process\tCompletion Time\tTurnaround Time\tWaiting Time")
    for process, completion_time in completed_processes:
        print(f"{process.pid}\t{completion_time}\t\t{process.turnaround_time}\t\t{process.waiting_time}")

    print(f"\nAverage Turnaround Time: {average_turnaround_time}")
    print(f"Average Waiting Time: {average_waiting_time}")
