from multiprocessing import Process
import os
import time


pid = os.fork()

if pid > 0:
    print('I am parent. My PID is ', os.getpid())
    time.sleep(0.1)
    
    print("Parent sleeping for 10 seconds...")
    time.sleep(10)
    print("Parent exiting now")

elif pid == 0:
    print("I am the child. My PID is ", os.getpid())
    os._exit(0)
