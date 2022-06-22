#%%

import time
import os
import multiprocessing
import threading

#%%
"""
More in depth notes on thread v process below...

https://stackoverflow.com/questions/18114285/what-are-the-differences-between-the-threading-and-multiprocessing-modules

- For python specific modules: 
    Global Interpreter Lock prevents two threads 
    in the same process from running Python code at the same time.

- There are exceptions to this. If your code's heavy computation 
    doesn't actually happen in Python, but in some library 
    with custom C code that does proper GIL handling, like a numpy app, 
    you will get the expected performance benefit from threading.

- Other times this works is when you want concurrency but not true
    core parallelism...one example would be having a network server
    go and retrieve packets while there's another thread responding to
    GUI app user inputs

- Using separate processes has no such problems with the GIL, 
    because each process has its own separate GIL. 

+--------------------------------------------------+
+           Active threads / processes             +
+-----------+--------------------------------------+
|Thread   1 |********     ************             |
|         2 |        *****            *************|
+-----------+--------------------------------------+
|Process  1 |***  ************** ******  ****      |
|         2 |** **** ****** ** ********* **********|
+-----------+--------------------------------------+
+           Time -->                               +
+--------------------------------------------------+
"""
#%%

#!/usr/bin/env python3

import multiprocessing
import threading
import time
import sys

def cpu_func(result, niters):
    '''
    A useless CPU bound function.
    '''
    for i in range(niters):
        result = (result * result * i + 2 * result * i * i + 3) % 10000000
    return result

class CpuThread(threading.Thread):
    def __init__(self, niters):
        super().__init__()
        self.niters = niters
        self.result = 1
    def run(self):
        self.result = cpu_func(self.result, self.niters)

class CpuProcess(multiprocessing.Process):
    def __init__(self, niters):
        super().__init__()
        self.niters = niters
        self.result = 1
    def run(self):
        self.result = cpu_func(self.result, self.niters)

class IoThread(threading.Thread):
    def __init__(self, sleep):
        super().__init__()
        self.sleep = sleep
        self.result = self.sleep
    def run(self):
        time.sleep(self.sleep)

class IoProcess(multiprocessing.Process):
    def __init__(self, sleep):
        super().__init__()
        self.sleep = sleep
        self.result = self.sleep
    def run(self):
        time.sleep(self.sleep)


cpu_n_iters = int(3)
sleep = 1
cpu_count = multiprocessing.cpu_count()
input_params = [
    (CpuThread, cpu_n_iters),
    (CpuProcess, cpu_n_iters),
    (IoThread, sleep),
    (IoProcess, sleep),
]
header = ['nthreads']
for thread_class, _ in input_params:
    header.append(thread_class.__name__)
print(' '.join(header))
for nthreads in range(1, 2 * cpu_count):
    results = [nthreads]
    for thread_class, work_size in input_params:
        start_time = time.time()
        threads = []
        for i in range(nthreads):
            thread = thread_class(work_size)
            threads.append(thread)
            thread.start()
        for i, thread in enumerate(threads):
            thread.join()
        results.append(time.time() - start_time)
    print(' '.join('{:.6e}'.format(result) for result in results))




#%%
"""
- Process: Basically the programs that are dispatched from the ready state and 
            are sceduled in the CPU for execution
    PCB: (Process Control Block): Holds the concept of a process
    - Processes can create other processes which are child processes
    - Processes can have states: 
        New:        New process is being created
        Ready:      Process is ready and waiting to be allocated to a processor
        Running:    Program is being executed
        Waiting:    Waiting for some event to occur
        Terminating: ? 
        Suspended:  Execution finished

- Thread: Segment of a process
    - Processes can have multiple threads
    - Each of these multiple threads in contained within a process
    - Thread can have three states:
        Running, Ready, Blocked

- Threads do not have isolated memory or compute
- Processes have isolated memory and compute (from other processes)
    - Processes have code, data, files, registers, and stack 
    - Threads share code, data, and resources

    - Processes havbe their own PCB, Stack, and Address space
    - Thread uses parent's PCB, it's own TCB, & address space
        but have their own stack, counter, and registers

    - All threads share same address space so changes on one thread to process
        level variable will affect all other threads

- We would need multi-programs to have multi-process, but one process
    is sufficient for multi-threading 

- In a multithreaded process on a single processor the processor can switch
    execution resources between threads, resulting in concurrent execution.
    Concurrency indicates that more than one thread is making progress, but the 
    threads are not actually running simultaneously...Switching happens quick 
    enough that the threads might appear to run simultaneously.

- However, in the same multi-threaded process in a shared-memory multi-processor
    environment each thread in the process can run concurrently on a separate 
    processor resulting in parallel/concurrent execution (true simultaneous execution)
    * - In Linux and most OS if the number of threads is less than or equal to the
            number of processes available the OS thread support system ensures
            each thread runs on a different processor...however in the real time
            embedded systems class we saw that sometimes we want to dispose of this
            and force threads to run at specific places given specific priorities
            to ensure they can meet deadlines *

- Thread synchronization (outside of python) is usually done via controlling variables
    that are stored in the shared address space:
        - Mutex locks: Allow only one thread at a time to execute a specific
                        section of code, or to access specific data
        - Read/Write lock: Permits concurrents reads and exclusive writes to a protected
                        shared resource. To modify that resource a thread must first 
                        acquire the exclusive write lock...this ewlock is not permitted
                        until all read locks have been released
        - Condition variables: Block threads until a certain condition is true
        - Counting Semaphore: Coordinate access to resources. Count is the limit on
                        how many threads can have concurrent access to the data protected
                        by the semaphore. When this count is reached the semaphore casues 
                        the calling thread to block until the count changes.
                        *Binary semaphore (count=1) is similar in operation to mutex lock
"""