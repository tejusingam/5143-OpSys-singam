# Chapter 3 Review Questions

Name: Tejaswi Singam

Course: 5143 Operating Systems

Date: 02 Mar 2016

## 3.4 What does it mean to preempt a process? 

When a process is moving from running state to ready state without the process requesting it is known as preempting a 

process.Preempt a process is based on priority. If a process has highest priority than the current running process then the 

current process is preempted or resumed and the highest priority process will execute first.

## 3.5 What is swapping and what is its purpose? 

Swapping is a memory management technique to maximize the process utilization by moving a process temporarily from 

main memory to secondary memory that is moving from ready state to ready suspend state. The purpose of swapping is to 

access data that is stored in hard disk and to bring it into the RAM so that it can be used by the application program. 

swapping is only necessary when that data is not already in the RAM.

## 3.9 List three general categories of information in a process 

##control block. 

The three general categories of  information in a process control block are

1.Process Identification

2.Process state Information

3.Process control Information

## 3.10 Why are two modes (user and kernel) needed? 

CPU has two different modes to run the processes.The processor switches between the two modes depending on the type 

of mode running on the processor.

**User mode** is non-privileged or non preemptive. All user programs and all application programs like audio, video,grapics runs 

in the user mode. The process has non-atomic execution(with preempt). Direct access of hardware is not allowed for the 

executing code. Code running in user mode must authorize to system APIs to access hardware or memory. Recovering the 

crashes occured in user mode is always possible due to this protection.Most of the code running on your computer will 

execute in user mode.

**Kernel Mode** is also known as system mode. It is priviliged, supervisory, protected and non-preemptive. OS services like

scheduler, dispatcher, memory manager and service routine runs under kernel mode. The process has non-atomic 

execution(without preemption).kernel mode shares a single virtual address space.Kernel mode is generally reserved for the 

lowest-level, most trusted functions of the operating system.Crashes in kernel mode are catastrophic,they will halt the 

entire PC.

## 3.12 What is the difference between an interrupt and a trap? 

Interrupt and Trap are the two events which will break down the execution of  the program.

**Trap** is a abnormal condition or an exception  caused  by an exception condition  (eg: division by zero)  was detected by CPU. 

**Interrupt** is a halt or an interruption in the normal execution of a program. When an interrupt occurs, the current process 

is stops its execution temporarily.

## 3.13 Give three examples of an interrupt.

The three examples of an interrupt are

1.Internal interrupts like Addressing error 

2.Page fault are like Debugging 

3.External Interrupt occurs when an I/O Device request for an Operation and the CPU will Execute that instructions first.

For Example When a Program is in execution and when the user move the Mouse on the Screen then the CPU will handle 

this External interrupt first and after that it will resume with the user Operation.

4.Software interupts like arithmetic errors.Software interrupts are caused either by an exceptional condition. This is also 

known as Trap or exception. For example, divide-by-zero exception. 

## 3.14 What is the difference between a mode switch and a process switch?

**Process switch** When the processor switches from one process to another.This causes the contents present in the cpu 

registers and instruction pointer were saved. The registers and instruction pointer for the new task will load into the 

processor and execution of the new process will start/resume. The old program is no longer executing, but it's state is 

saved in memory for when the kernel decides that it is ready to execute it again. This is what gives the illusion of 

multitasking, while in reality, only a single process can run at a time on a cpu. A context switch can occur by hardware 

or software. A hardware interrupt can occur from a device such as the keyboard,mouse,or system timer, causing code to

begin executing the interrupt code.

**Mode switch** It switch the process privilege between the mode like use mode, kernel mode. Generally a mode switch is 

considered less expensive compared to a process switch. A mode switch is what is referred to when the cpu changes 

privilege levels. The kernel works at a higher privilege than a standard user task. In order for the user task to access 

things controlled by the kernel, it is necessary fro a mode switch to occur. The currently executing process does not 

change during a mode switch. The processor uses these modes to protect the OS from misbehaving or malicious programs, 

as well as controlling concurrent access to ram, io devices,etc. A mode switch must occur for a software context switch 

to occur.

