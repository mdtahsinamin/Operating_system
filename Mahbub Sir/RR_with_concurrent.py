import concurrent.futures
import matplotlib.pyplot as plt

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

        entry_time = current_time

        # Calculate completion time
        self.completion_time = current_time + self.burst_time

        # Calculate turnaround time and waiting time
        self.turnaround_time = self.completion_time - self.arrival_time
        self.waiting_time = self.turnaround_time - self.burst_time

        return entry_time, self.completion_time

def fcfs_scheduler(processes):
    current_time = 0
    gantt_chart_entries = []

    completed_processes = []

    for process in processes:
        entry_time, completion_time = process.run(current_time)
        current_time = completion_time
        completed_processes.append(process)
        gantt_chart_entries.append((entry_time, completion_time))

    return completed_processes, gantt_chart_entries

def plot_gantt_chart(gantt_entries):
    plt.figure(figsize=(10, 4))
    plt.ylim(0, len(gantt_entries))
    plt.xlabel("Time")
    plt.ylabel("Process")

    for i, (entry_time, completion_time) in enumerate(gantt_entries):
        plt.barh(i, completion_time - entry_time, left=entry_time, align='center', label=f"Process {i + 1}")

    plt.yticks(range(len(gantt_entries)), [f"Process {i + 1}" for i in range(len(gantt_entries))])
    plt.legend()
    plt.title("Gantt Chart - FCFS Scheduling")
    plt.show()

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
        completed_processes, gantt_chart_entries = fcfs_scheduler(processes)

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

    plot_gantt_chart(gantt_chart_entries)
