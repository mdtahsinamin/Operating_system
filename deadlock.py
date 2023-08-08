import numpy as np

def bankersAlgorithm(avaiable, Allocattion, Max):
    work = avaiable
    n = len(Allocattion)
    finish = [False for i in range(n)]
    need = np.subtract(Max, Allocattion)

    process_done = []
    process_incomplete= n

    while True:
       if process_incomplete <=0:
           print("Safe sequence : ")
           for i in range(len(process_done)):
               print(process_done[i])
           break

       for i in range(n):
           if finish[i] == False and all(np.less_equal(need[i], work)):
               finish[i] = True
               work = np.add(work, Allocattion[i])
               process_done.append(i)
               process_incomplete-=1

       if len(process_done) <=0:
           print('Deadlock')
           break





available = np.array([0, 0 , 0])

Allocation = np.array([
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
])
Max = np.array([
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
])

bankersAlgorithm(available, Allocation, Max)