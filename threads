## Name : TEJASWI SINGAM ##
## Date : 04/08/2016 ##
## MID  : M20220899 ##

1. In thread2.py ,the shared counter variable is used. This shared counter increment operation executes in three steps. First  the current value of the shared counter is fetched by the interpreter and then it calculates the new value. At last this value is stored back in the variable. The counter value will not be accurate if this function call is done by more than one thread.    
When  current value is fetched by one thread, if the other thread gets control then it fetches the current value and calculates the new value and store backs that value in the variable before the current thread does the things. Inconsistence problem  occurs when two or more threads executes.
In thread1.py, this shared counter variable is not used. Here the atomic operations are performed where the execution can be done in one step without allowing the other thread to get control.

