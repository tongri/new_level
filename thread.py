from threading import Thread, Lock
import time

lock = Lock()



def f(i):
    print(f'thread {i} is laucnhed')
    time.sleep(4)
    lock.acquire()
        #time.sleep(4)
    
    print(f'thread number {i} is back')
    
    lock.release()

threads = list()

for i in range(10):
    threads.append(Thread(target=f, args=(i, )))
    threads[i].start()


for thread in threads:
    thread.join()
