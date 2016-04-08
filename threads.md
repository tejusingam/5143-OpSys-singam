## Name : TEJASWI SINGAM ##
## Date : 04/08/2016 ##
## MID  : M20220899 ##

#### 1. Explain the differences between Threads1 and Threads2 using lines from the code and a precise explanation.

In thread2.py ,the shared counter variable is used. This shared counter increment operation executes in three steps. First the current value of the shared counter is fetched by the interpreter and then it calculates the new value. At last this value is stored back in the variable.The counter value will not be accurate if this function call is done by more than one thread. When  current value is fetched by one thread, if the other thread gets control then it fetches the current value and calculates the new value and store backs that value in the variable before the current thread does the things. Inconsistence problem  occurs when two or more threads executes.

In thread1.py, this shared counter variable is not used. Here the atomic operations are performed where the execution can be done in one step without allowing the other thread to get control.

#### 2. After running Thread3.py does it fix the problems that occured in Threads2.py? What's the down-side?

In thread3.py, the lock concept is used. locks are the one of the synchronization mechanism which is used to synchronize access to a shared resources. Lock object is created and acquire call is performed to hold the lock and release operation is performed to release the lock. This concept overcome the inconsistency problem which we have seen in Threads2.py and only one thread can access the resources at a time. There is no conflicts or duplications will occur.

#### 3. Comment out the join statements at the bottom of the program and describe what happens.

If we comment out join method then, main threads gets terminated before the threads A and B terminates.

#### 4. What happens if you try to Ctrl-C out of the program before it terminates?

When the Ctrl-C button is entered the keyboard interrupt message is displayed.

#### 5. Read and run Threads4.py. This generates a different and more ridiculous race condition. Write concise explanation of what's happening to cause this bizarre behavior using lines from the code and precise explanation.

In thread4.py, the lock operations which are acquire and release operations are not performed. So the threads will not execute in order. the resouces can be accessed by all threads at a time. 

#### 6. Does uncommenting the lock operations clear up the problem in question 5?
 If we uncommenting the lock operations then acquire operation will hold the resources until the previous thread releases. So the thread will not get the resources until the current thread releases the resources.



