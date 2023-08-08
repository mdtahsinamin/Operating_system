# non-preemptive
def non_preemptive_sjf(processes, burst_time):
    n = len(processes)
    completion_time = [0] * n
    waiting_time = [0] * n
    turn_around_time = [0] * n
    total_waiting_time = 0
    total_turn_around_time = 0

    # Sort processes based on burst time
    sorted_processes = sorted(processes, key=lambda x: burst_time[x - 1])

    current_time = 0
    for process in sorted_processes:
        completion_time[process - 1] = current_time + burst_time[process - 1]
        turn_around_time[process - 1] = completion_time[process - 1]
        waiting_time[process - 1] = turn_around_time[process - 1] - burst_time[process - 1]
        current_time = completion_time[process - 1]

        total_waiting_time += waiting_time[process - 1]
        total_turn_around_time += turn_around_time[process - 1]

    avg_waiting_time = total_waiting_time / n
    avg_turn_around_time = total_turn_around_time / n

    return completion_time, turn_around_time, waiting_time, avg_turn_around_time, avg_waiting_time

#preemptive
def round_robin(processes, burst_time, time_quantum):
    n = len(processes)
    remaining_burst_time = list(burst_time)
    completion_time = [0] * n
    waiting_time = [0] * n
    turn_around_time = [0] * n
    total_waiting_time = 0
    total_turn_around_time = 0

    current_time = 0
    while any(rt > 0 for rt in remaining_burst_time):
        for i in range(n):
            if remaining_burst_time[i] > 0:
                if remaining_burst_time[i] <= time_quantum:
                    current_time += remaining_burst_time[i]
                    completion_time[i] = current_time
                    remaining_burst_time[i] = 0
                else:
                    current_time += time_quantum
                    remaining_burst_time[i] -= time_quantum

    for i in range(n):
        turn_around_time[i] = completion_time[i]
        waiting_time[i] = turn_around_time[i] - burst_time[i]

        total_waiting_time += waiting_time[i]
        total_turn_around_time += turn_around_time[i]

    avg_waiting_time = total_waiting_time / n
    avg_turn_around_time = total_turn_around_time / n

    return completion_time, turn_around_time, waiting_time, avg_turn_around_time, avg_waiting_time


if __name__ == "__main__":
    processes = [1, 2, 3, 4, 5]
    burst_time = [5, 3, 1, 7, 4]
    priority = [4, 1, 2, 2, 3]
    time_quantum = 2

    # Non-preemptive SJF Scheduling
    sjf_completion, sjf_turnaround, sjf_waiting, sjf_avg_turnaround, sjf_avg_waiting = non_preemptive_sjf(processes, burst_time)

    print("Non-Preemptive SJF Scheduling:")
    print("Process\tCompletion Time\tTurnaround Time\tWaiting Time")
    for i, process in enumerate(processes):
        print(f"{process}\t{sjf_completion[i]}\t\t{sjf_turnaround[i]}\t\t{sjf_waiting[i]}")
    print(f"Avg Turnaround Time: {sjf_avg_turnaround:.2f}")
    print(f"Avg Waiting Time: {sjf_avg_waiting:.2f}\n")



    # Preemptive Round Robin Scheduling
    rr_completion, rr_turnaround, rr_waiting, rr_avg_turnaround, rr_avg_waiting = round_robin(processes, burst_time, time_quantum)

    print("Preemptive Round Robin Scheduling:")
    print("Process\tCompletion Time\tTurnaround Time\tWaiting Time")
    for i, process in enumerate(processes):
        print(f"{process}\t{rr_completion[i]}\t\t{rr_turnaround[i]}\t\t{rr_waiting[i]}")
    print(f"Avg Turnaround Time: {rr_avg_turnaround:.2f}")
    print(f"Avg Waiting Time: {rr_avg_waiting:.2f}")