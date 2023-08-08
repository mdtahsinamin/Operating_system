import matplotlib.pyplot as plt

n = int(input("Enter number of process : "))
arrival_time = []
burst_time = []
turnaround_time = []
waiting_time = []
time_entry = []
completion_time=[]
process_sequence = []

system_idel = 0


time = 0

print("Enter arrival time: \n")
for i in range(n):
    x = float(input())
    arrival_time.append(x)

print("Enter burst time: \n")
for i in range(n):
    y = float(input())
    burst_time.append(y)

for i in range(n):

    if time < arrival_time[i]:
        system_idel += abs(time - arrival_time[i])
        time = arrival_time[i]

    process_sequence.append(i)
    time_entry.append(time)
    time = time + burst_time[i]
    completion_time.append(time)

for i in range(n):
    turnaround_time.append(completion_time[i] - arrival_time[i])
    waiting_time.append(turnaround_time[i] - burst_time[i])

print(turnaround_time, waiting_time)
plt.barh(y=process_sequence, width=completion_time, left=time_entry)
plt.show()