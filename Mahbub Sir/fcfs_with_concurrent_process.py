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

def fcfs_scheduler(processes):
    current_time = 0
    completion_times = []

    for process in processes:
        completion_time = process.run(current_time)
        completion_times.append(completion_time)
        current_time = completion_time

    return completion_times

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
        completion_times = fcfs_scheduler(processes)

    total_turnaround_time = 0
    total_waiting_time = 0
    for process in processes:
        total_turnaround_time += process.turnaround_time
        total_waiting_time += process.waiting_time

    average_turnaround_time = total_turnaround_time / len(processes)
    average_waiting_time = total_waiting_time / len(processes)

    print("Process\t Completion Time\tTurnaround Time\tWaiting Time")
    for process, completion_time in zip(processes, completion_times):
        print(f"{process.pid}\t \t {completion_time}\t\t\t\t\t\t\t{process.turnaround_time}\t\t\t{process.waiting_time}")

    print(f"\nAverage Turnaround Time: {average_turnaround_time}")
    print(f"Average Waiting Time: {average_waiting_time}")

