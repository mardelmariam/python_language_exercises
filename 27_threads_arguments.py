#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 10:49:07 2025

@author: maryam
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 10:46:53 2025

@author: maryam
"""

from time import sleep
from threading import Thread


def task(sleep_time, message):
    sleep(sleep_time)
    print(message)
    

thread = Thread(target=task, args=(3, 'New message from another thread...'))

thread.start()

print('Waiting for the thread...')
# Wait for the thread to finish
thread.join()
print('Task finished.')
