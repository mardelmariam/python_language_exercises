# -*- coding: utf-8 -*-

from time import sleep
from threading import Thread

def task():
    sleep(1)
    print('This is another thread...')
    
thread = Thread(target=task)

thread.start()

print('Waiting for the thread...')
# Wait for the thread to finish
thread.join()
print('Task finished.')
