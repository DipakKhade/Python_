# Time Module in Python | Python Tutorial - Day #84

import time

# def usingwhile():
#     i=0
#     while i<200:
#         i=i+1
#         print(i)

# def usingfor():
#     for i in range(0,200):
#         print(i)

# init=time.time()
# usingfor()
# print(time.time()-init)

# init=time.time()
# usingwhile()
# print(time.time()-init)




# time.sleep()                        slpeeping time
# print(4)
# print(time.sleep(3))
# print('This is printed afther 3 sec')



# time.localtime()                      date and time   
t=time.localtime()
formated_time=time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formated_time)




 



    
