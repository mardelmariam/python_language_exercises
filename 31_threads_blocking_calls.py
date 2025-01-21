#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 12:23:10 2025

@author: maryam
"""


"""

A blocking call if a function call that does not return until it is complete.

All normal functions are blocking calls. 

In concurrent programming, blocking calls are calls to functions that will
wait for a specific condition and signal to the operating system that 
nothing interesting is going on while the thread is waiting. Then, the
operating system may notice that a thread is making a blocking function call
and dedice to context switch to another thread.

The operating system prefers to switch away from blocked threads, allowing
non-blocked threads to run.

"""

#%%

"""

Examples of blocking calls:
    
To be continued...

"""