#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 11:24:02 2025

@author: maryam
"""

from threading import Thread
from time import sleep

thread = Thread(target=lambda:sleep(1))

# Thread's name
print(thread.name)

# A daemon thread is a background thread. By default, threads are non-daemon
# threads
print(thread.daemon)

# Status
print(thread.is_alive())


# Thread ID
print(thread.ident)
print('Thread start')
thread.start()
print(thread.ident)
print(thread.native_id)
print(thread.is_alive())

thread.join()
print('Thread finish')
print(thread.is_alive())


#%%

from threading import Thread

thread = Thread(name='MyThread')
print(thread.name)

thread.name='Hilo'
print(thread.name)


#%%

"""
The main thread is the defaukt thread created for each Python process.
In normal conditions, the main thread is the thread from which the Python
interpreter was started.

"""

# Using the main thread
from threading import main_thread
# Using any thread, including the main thread
from threading import current_thread

# Get the main thread
thread = main_thread()
print(f'name={thread.name}, id={thread.ident}')
thread2 = current_thread()
print(f'name={thread2.name}, id={thread2.ident}')


#%%

"""
A background (daemon) thread will not have control over when it is terminated

The program will terminate once all non-background threads finish, even if 
there are background tasks running. Therefore, the code it executes must be
robust to arbitrary termination, such as the flushing and closing of external
resources like streams and files that may be not be closed correctly.

In Python, a process will exit if only background threads are running.


"""

from threading import Thread

thread = Thread(daemon=True)
# The daemon property can only be set on a thread when it's not running
# thread.daemon = True
print(thread.daemon)

#%%

from time import sleep
from threading import current_thread
from threading import Thread
 
def task():
    thread = current_thread()
    print(f'Daemon thread: {thread.daemon}')
 
thread = Thread(target=task, daemon=True)
thread.start()
sleep(0.5)

#%%

from time import sleep
from threading import current_thread
from threading import Thread
 
# function to be executed by second daemon thread
def task2():
    thread = current_thread()
    print(f'Daemon thread 2: {thread.daemon}')
 
# function to be executed in a new thread
def task():
    thread = current_thread()
    print(f'Daemon thread 1: {thread.daemon}')
    new_thread = Thread(target=task2)
    new_thread.start()
 
# create a new daemon thread
thread = Thread(target=task, daemon=True)
# start the new thread
thread.start()
# block for a moment to let the daemon threads run
sleep(0.5)


#%% Thread utilities

import threading

print(threading.active_count())
threads = threading.enumerate()

for thread in threads:
    print(thread.name)
    
    
#%% Using exceptions

from time import sleep
from threading import Thread
 
# target function that raises an exception
def work():
    print('Working...')
    sleep(1)
    # rise an exception
    raise Exception('Something bad happened')
 
thread = Thread(target=work)

thread.start()
thread.join()
print('Continuing on...')

#%% Exception hooks

from time import sleep
import threading
 
# target function that raises an exception
def work():
    print('Working...')
    sleep(1)
    # rise an exception
    raise Exception('Something bad happened')
 
# custom exception hook
def custom_hook(args):
    # report the failure
    print(f'Thread failed: {args.exc_value}')
 
# set the exception hook
threading.excepthook = custom_hook

# create a thread
thread = threading.Thread(target=work)
thread.start()
thread.join()
print('Continuing on...')


#%% Limitations of threads

"""
The CPython Python interpreter generally does not permit more than one thread
to run at a time. This is achieved through a mutual exclusion (mutex) lock 
(also called Global Interpreter Lock - GIL)
within the interpreter that ensures that only one thread a a time can execute
Python bytecodes in the Python virtual machine.

This lock prevents race conditions and ensures thread safety.

Sometimes, this lock is released by the interpreter for certain libraries
that need longer compute times, like Numpy or Pandas. A momentary release
allows running codes in parallel. However, it's important to underscore that
threads are not made for parallel computing.

"""

#%% When to use a thread

"""

1. When a thread is performing blocking IO: reading from or writing to a device,
    file, socket, connection. or database.
    The GIL is released, and this frees the microprocessor for 
    running other threads.
2. When a thread is executing C code and explicitly releases the lock

Avoiding the lock entirely:
    
Using another Python interpreter to execute Python code

"""





