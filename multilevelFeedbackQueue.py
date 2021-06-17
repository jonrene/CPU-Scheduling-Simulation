# Given process data
ProcessData = [
    [5, 27, 3, 31, 5, 43, 4, 18, 6, 22, 4, 26, 3, 24, 4],
    [4, 48, 5, 44, 7, 42, 12, 37, 9, 76, 4, 41, 9, 31, 7, 43, 8],
    [8, 33, 12, 41, 18, 65, 14, 21, 4, 61, 15, 18, 14, 26, 5, 31, 6],
    [3, 35, 4, 41, 5, 45, 3, 51, 4, 61, 5, 54, 6, 82, 5, 77, 3],
    [16, 24, 17, 21, 5, 36, 16, 26, 7, 31, 13, 28, 11, 21, 6, 13, 3, 11, 4],
    [11, 22, 4, 8, 5, 10, 6, 12, 7, 14, 9, 18, 12, 24, 15, 30, 8],
    [14, 46, 17, 41, 11, 42, 15, 21, 4, 32, 7, 19, 16, 33, 10],
    [4, 14, 5, 33, 6, 51, 14, 73, 16, 87, 6]
]
# List of processes currently in ready state
Ready = []
# List of proceses currently using CPU
CPU = []
# List of processes currently in IO state
IO = []
# List of processes that have finished
Finished = []
# Keeps track of current time
GLOBALTIME = 0

# defines a process and all its properties
class Process:
    def __init__(self, info, name):
        self.name = name
        self.bursts = info
        self.wait_time = 0
        self.turn_around = 0
        self.response_time = 0
        self.back_to_ready = 0
        self.first_time = True
        self.queue = 1


# Creates all new process (P1-P8) and puts it in Ready list
P1 = Process(ProcessData[0], "P1")
Ready.append(P1)
P2 = Process(ProcessData[1], "P2")
Ready.append(P2)
P3 = Process(ProcessData[2], "P3")
Ready.append(P3)
P4 = Process(ProcessData[3], "P4")
Ready.append(P4)
P5 = Process(ProcessData[4], "P5")
Ready.append(P5)
P6 = Process(ProcessData[5], "P6")
Ready.append(P6)
P7 = Process(ProcessData[6], "P7")
Ready.append(P7)
P8 = Process(ProcessData[7], "P8")
Ready.append(P8)

#Prints dynamic info
def dynamic():
  #prints current execution time
  print(f"\nCurrent Execuation Time: {GLOBALTIME}")
  #prints process currently running
  print(f"Running process: {CPU[0].name}")
  print(" \n")
  #prints processes in ready queue and their next cpu burst
  print("Processes in Ready Queue")
  if len(Ready) > 0:
    for x in Ready:
      print(x.name,'-', x.bursts[0], 'time units in next burst')
  else:
    print("None")
    print('-----------------------------------')
  print('\n')
  #prints processes getting IO and time until finished with IO
  print("Processes in I/O")
  if len(IO) > 0:
    for x in IO:
      print(x.name,'-', x.back_to_ready-GLOBALTIME, 'time units until finished with I/O' )
    print('-----------------------------------')
  else:
    print("None")
    print('-----------------------------------')

# increases wait time of all processes in ready list
def increase_wait_time():
    for x in Ready:
        x.wait_time += 1


# Sends any process that is done with IO burst time back to ready list
def return_to_ready():
    if len(IO) > 0:
        go_back = []
        # finds all process that are done getting IO
        for x in range(len(IO)):
            if IO[x].back_to_ready == GLOBALTIME:
                go_back.append(x)
        # sends all processes getting IO back to ready list
        for x in sorted(go_back, reverse=True):
            Ready.append(IO.pop(x))
        #sorts ready list based on level of Process
        Ready.sort(key=lambda x: x.queue)


# main function
if __name__ == "__main__":
    #sorts Ready list based on queue level of all processes
    Ready.sort(key=lambda x: x.queue)
    #checks if all processes are completed
    while (len(Finished) != len(ProcessData)):
        # checks if CPU is being used and if a process is ready
        # if CPU free and a process is ready, add next ready program to CPU
        if ((len(CPU) == 0) and (len(Ready) != 0)):
            # add next ready program to cpu
            CPU.append(Ready.pop(0))
            # Gets response time of process if first time on CPU
            if ((CPU[0].first_time == True)):
                CPU[0].response_time = GLOBALTIME
                CPU[0].first_time = False
            #prints dynamic info
            dynamic()
            # Executes round robin with Tq = 5 if current process in queue 1
            if CPU[0].queue == 1:
                #checks if CPU burst will be greater than 5 time units for Queue 1
                if CPU[0].bursts[0] > 5:
                    CPU[0].queue = 2  # downgrades process to queue 2
                    CPU[0].bursts[0] -= 5  #removes 5 time units from current cpu burst of current process
                    for _ in range(5):
                        GLOBALTIME += 1  #increases global time
                        increase_wait_time()  # increases wait time for all ready processes
                        return_to_ready()  #sends process done with IO back to ready queue
                    Ready.append(CPU.pop(0))  # sends current process back to ready queue
                    Ready.sort(key=lambda x: x.queue)  # sorts ready queue based on queue

                # executes current cpu burst if less than 5 time units
                else:
                    for _ in range(CPU[0].bursts[0]):
                        GLOBALTIME += 1  #increases global time
                        increase_wait_time()  # increases wait time for all ready processes
                        return_to_ready()  #sends process done with IO back to ready queue

                    #gets rid of current cpu burst of current process (no longer needed)
                    CPU[0].bursts.pop(0)
                    # sends current process to finished list if finished
                    if len(CPU[0].bursts) == 0:
                        CPU[0].turn_around = GLOBALTIME
                        #prints that process is finished
                        print(f"Process {CPU[0].name} has finished at time {GLOBALTIME}")
                        Finished.append(CPU.pop(0))
                    # sends current process to IO if not finished
                    else:
                        CPU[0].back_to_ready = CPU[0].bursts[0] + GLOBALTIME
                        CPU[0].bursts.pop(0)
                        IO.append(CPU.pop(0))

            # Executes round robin with Tq = 10 if current process in queue 2
            elif CPU[0].queue == 2:
                #checks if CPU burst will be greater than 10 time units for Queue 1
                if CPU[0].bursts[0] > 10:
                    CPU[0].queue = 3  # downgrades process to queue 3
                    CPU[0].bursts[0] -= 10  #removes 5 time units from current cpu burst of current process
                    for _ in range(10):
                        GLOBALTIME += 1  #increases global time
                        increase_wait_time()  # increases wait time for all ready processes
                        return_to_ready()  #sends process done with IO back to ready queue
                    Ready.append(CPU.pop(0))  # sends current process back to ready queue
                    Ready.sort(key=lambda x: x.queue)  # sorts ready queue based on queue

                # executes current cpu burst if less than 10 time units
                else:
                    for _ in range(CPU[0].bursts[0]):
                        GLOBALTIME += 1  #increases global time
                        increase_wait_time()  # increases wait time for all ready processes
                        return_to_ready()  #sends process done with IO back to ready queue

                    #gets rid of current cpu burst of current process (no longer needed)
                    CPU[0].bursts.pop(0)
                    # sends current process to finished list if finished
                    if len(CPU[0].bursts) == 0:
                        CPU[0].turn_around = GLOBALTIME
                        #prints that process is finished
                        print(f"Process {CPU[0].name} has finished at time {GLOBALTIME}")
                        Finished.append(CPU.pop(0))
                    # sends current process to IO if not finished
                    else:
                        CPU[0].back_to_ready = CPU[0].bursts[0] + GLOBALTIME
                        CPU[0].bursts.pop(0)
                        IO.append(CPU.pop(0))

            # executes FCFS if process is in queue 3
            else:
                #starts cpu burst for process in CPU
                for _ in range(CPU[0].bursts[0]):
                    #increases global time
                    GLOBALTIME += 1
                    # increases wait time for all ready processes
                    increase_wait_time()
                    #sends processes from IO quee that need to go back to ready que back to ready que
                    return_to_ready()

                #gets rid of current cpu burst of current process (no longer needed)
                CPU[0].bursts.pop(0)
                # sends current process to finished list if finished
                if len(CPU[0].bursts) == 0:
                    CPU[0].turn_around = GLOBALTIME
                    #prints that process is finished
                    print(f"Process {CPU[0].name} has finished at time {GLOBALTIME}")
                    Finished.append(CPU.pop(0))
                # sends current process to IO if not finished
                else:
                    CPU[0].back_to_ready = CPU[0].bursts[0] + GLOBALTIME
                    CPU[0].bursts.pop(0)
                    IO.append(CPU.pop(0))

        # Increases time for all processes in IO list if all unfinished processes are in IO
        else:
            GLOBALTIME += 1
            return_to_ready()

    #calculates total wait time
    TW = 0
    for x in Finished:
        TW += x.wait_time
    #calculates total turnaround time
    TTR = 0
    for x in Finished:
        TTR += x.turn_around
    #calculates total response time
    TR = 0
    for x in Finished:
        TR += x.response_time

    # printing results of simulation
    #prints total execution time
    print(f"Total Execution Time: {GLOBALTIME}")

    #prints cpu utilization
    print(f"CPU Utilization: {round((553/GLOBALTIME)*100,2)}%")

    #prints waiting time, turnaround time, and respose time for every process and average values
    print('\n')
    Finished.sort(key=lambda x: x.name)
    print("     Tw", "      Ttr", "    Tr") 
    for x in Finished:
        print(f"{x.name:<4}", f"{x.wait_time:<8}", f"{x.turn_around:<7}",
              x.response_time)
    print("Avg ", f"{round((TW/8),2):<8}", f"{round((TTR/8),2):<7}",
          round((TR / 8), 2))
