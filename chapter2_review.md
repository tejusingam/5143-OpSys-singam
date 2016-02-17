# Chapter 2 Review Questions

Name: Singam Tejaswi

Course: 5143 Operating Systems

Date:17 Feb 2016

## 1.What are three objectives of an OS design?

The three objectives of an OS design are

•	Convenience

•	Efficiency 

•	Ability to evolve

## 2.What is the kernel of an OS?

kernel is the central part of an operating system that controls  input and output operations from  the software, and interpret  

them into data processing instructions for the CPU.

## 3.What is multiprogramming?

The process of executing two or more programs on single processor machine  simultaneously.

## 4.What is a process?

A process is a program in execution state.

## 5.How is the execution context of a process used by the OS?

the process state or a execution context helps the operating system to control and manage a process. It is the internal data 

and it incorporates the content of various process registers  and the process priority information and if the process is waiting 

for the completion of a particular input output operations.

## 6.List and briefly explain five storage management responsibilities of a typical OS.

Five storage management responsibilities of an OS are 

•	**Process isolation** 

The operating system will helps to prevent the interleaving  with other processes memory, data and memory.

•	**Automatic allocation and  management**

Programs should be dynamically allocated across the memory hierarchy as required. Allocation should be transparent 

to the programmer. Thus, the programmer is relieved of concerns relating to memory limitations, and the operating system 

can achieve efficiency by assigning memory to jobs only as needed..

•	**Support of modular programming**

Program  modules can be able to define by the programmers  and to create, destroy and alter the size of the module 

dynamically.

•	**Protection and access control**

One program can able to address the memory space of other by sharing the memory at any level of  the memory hierarchy. 

This is an dvantage when  a particular application  is  needed  the  sharing of  memory. 

•	**Long term storage**

Application programs should be stored for long period of time even after the system  powered down.. This can be achieved  by 

virtual memory and file system facilities. a long-term storage is implemented by file system  along with the information is 

stored in the format of  named objects. These objects are known as files.

## 7.Explain the distinction between a real address and a virtual address.

Real addresses refer to hardware addresses of physical memory and Virtual address is a reference to the program in the 

main memory. Real address ranges from (R+0 to R+max) where R is the base value and Virtual address ranges from 0 to 

max.

## 8.Describe the round-robin scheduling technique.

Round robin technique is simple and most frequently  used algorithm.In this technique, processes are dispatched in a FIFO manner but are given a limited amount of CPU time called a time-slice or a quantum. If a process does not complete before the time expires, the CPU is preempted and given to the next process waiting in a queue. The preempted process is then placed at the back of the ready list. Round Robin Scheduling is preemptive (at the end of time-slice) therefore it is effective in time-sharing environments in which the system needs to guarantee reasonable response times for interactive users. The only interesting issue with round robin scheme is the length of the quantum. Setting the quantum too short causes too many context switches and lower the CPU efficiency. On the other hand, setting the quantum too long may cause poor response time and approximates FCFS.

## 9.Explain the difference between a monolithic kernel and a microkernel.

**Monolithic kernel**

Monolithic Kernels is the older approach and it will supports all OS functionalities in kernel space.

It runs every basic system service like process and memory management, interrupt handling and I/O communication, 

file system, etc.

One of the main advantage is it provides good performance

Some of the disadvantages are

. Dependencies between system component like same address space provided.

. Complex & huge millions of lines of code.

. Larger size makes it hard to maintain.

  Examples- Multics, Unix, Linux
  
**microkernel**
  
Microlithic Kernels will supports only few functions like 

Interprocess communication.

Virtual memory.

Thread Scheduling.

And some other like Device drivers, networking, file system, user interface are kept in the user space.

Advantage of microkernel is it has more stability with less OS services in kernal space.

Disadvantage of microkernel is it has lots of system calls and context switches

Example- Mach, L4, Minix, K42

## 10.What is multithreading?

Multithreading is the ability of a cpu to execute multiple processes or threads concurrently.

## 11.List the key design issues for an SMP operating system.

•	Simultaneous concurrent processes or threads.

•	Scheduling.

•	Synchronization.

•	Memory management.

•	Reliability and fault tolerance.



