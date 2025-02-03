import threading
import time
def task():
    print("task started")
    time.sleep(2)
    print("task done")

def task1():
    print("task 1 started")
    time.sleep(2)
    print("task 1 done")

thread1=threading.Thread(target=task)
thread2=threading.Thread(target=task1)
thread1.start()
thread1.join()
thread2.start()
thread1.join()
print("execution done")