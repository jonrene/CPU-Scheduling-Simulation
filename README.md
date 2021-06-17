# CPU-Scheduling-Simulation

Introduction

	In this project, three different CPU scheduling algorithms will be implemented using a desired programming language. In this case, Python. The three different CPU scheduling algorithms that will be implemented are: first come first served (FCFS), shortest job first (SJF), and multilevel feedback queue (MLFQ). Once implemented, each scheduling algorithm will be simulated using eight different process, each containing different amounts of CPU and I/O bursts. The simulation for each scheduling algorithm will include calculating the overall CPU utilization and the total and average, waiting time, turnaround time, and response time for all eight processes. The performance of each scheduling algorithm will then be evaluated and compared. The objective of this assignment is to learn more about OS scheduling through a hands-on simulation programming experience.
	Each of the CPU scheduling algorithms that will be implemented will be done so with the following assumptions:

1.	All processes are activated at time 0
2.	Assume that no process waits on I/O devices.
3.	After completing an I/O event, a process is transferred to the ready queue.
4.	Waiting time is accumulated while a process waits in the ready queue.
5.	Turnaround time is a total of (Waiting time) + (CPU burst time) + (I/O time)
6.	Response time is the first measure of waiting time from arrival at time 0 until the first time on the CPU.

For the implementation of the multilevel feedback queue, it will be implemented using the following structure:

•	Queue 1 uses RR scheduling with Tq = 5
•	Queue 2 uses RR scheduling with Tq = 10
•	Queue 3 uses FCFS

Also, higher queues will have absolute priority and all process will initially be entered into the first queue. A process is downgraded to next lower priority queue if time quantum (Tq) expires before CPU burst is complete and will not be upgraded once it has been downgraded. 


Methodology

	The varying CPU scheduling algorithms will be implemented using Repl.it. This is an online integrated development environment. Each CPU algorithm implementation will be coded separately. This means three different programs. The given information on the eight different processes, CPU and I/O bursts, will be hard coded into each program. Once each program is written, one simply has to run the program on the Repl.it IDE. Both dynamic and final information for the eight processes will print to screen for each respective CPU algorithm. 



Data

	Below is the given data for the eight processes that will be used to simulate the three different CPU scheduling algorithms. Here is the format of the given processes: 
Process Name/Number {CPU burst, I/O time, I/O time,........, last CPU burst} 
P1 {5, 27, 3, 31, 5, 43, 4, 18, 6, 22, 4, 26, 3, 24, 4}
P2 {4, 48, 5, 44, 7, 42, 12, 37, 9, 76, 4, 41, 9, 31, 7, 43, 8}
P3 {8, 33, 12, 41, 18, 65, 14, 21, 4, 61, 15, 18, 14, 26, 5, 31, 6}
P4 {3, 35, 4, 41, 5, 45, 3, 51, 4, 61, 5, 54, 6, 82, 5, 77, 3}
P5 {16, 24, 17, 21, 5, 36, 16, 26, 7, 31, 13, 28, 11, 21, 6, 13, 3, 11, 4}
P6 {11, 22, 4, 8, 5, 10, 6, 12, 7, 14, 9, 18, 12, 24, 15, 30, 8}
P7 {14, 46, 17, 41, 11, 42, 15, 21, 4, 32, 7, 19, 16, 33, 10}
P8 {4, 14, 5, 33, 6, 51, 14, 73, 16, 87, 6
