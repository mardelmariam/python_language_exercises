#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 11:12:14 2025

@author: maryam
"""

from time import sleep
from threading import Thread

class CustomThread(Thread):
    
    # Override the constructor
    def __init__(self, value):
        Thread.__init__(self)
        self.value = value
        
    # Override the run function
    def run(self):
        sleep(self.value)
        print(f'This is coming from another thread: {self.value}')
        self.value = 3.0
        

thread = CustomThread(2.5)
thread.start()

print('Waiting for the thread...')
# Wait for the thread to finish
thread.join()
print('Task finished.')
print(f'Got value: {thread.value}')
