# Multithreading in Python | Python Tutorial - Day #97

import threading

import time

# indicates some task is being done
def fun(seconds):
    print(f'sleeping for {seconds} seconds')
    time.sleep(seconds)

# normal code
# fun(2)
# fun(6)
# fun(7)

time1=time.time()

# same code using Thread

t1=threading.Thread(target=fun,args=[2])
t2=threading.Thread(target=fun,args=[6])
t3=threading.Thread(target=fun,args=[7])

t1.start()
t2.start()
t3.start()

time2=time.perf_counter()
print(time2-time1)
