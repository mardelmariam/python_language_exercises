#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 10:51:20 2025

@author: maryam
"""

from time import sleep
from threading import Thread


"""
Extending a class allows data to be stored as instance variables and accessed
by a new thread, as well as data created by the new thread to be retrieved as
instance variables
"""
class CustomThread(Thread):
    
    #Override the run function
    def run(self):
        sleep(1)
        print('This is coming from another thread...')
        

thread = CustomThread()
thread.start()

print('Waiting for the thread...')
# Wait for the thread to finish
thread.join()
print('Task finished.')
