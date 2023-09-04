# Exercise 2: Good Morning Sir | Python Tutorial - Day #15

import time

'''a=(time.gmtime())
b=time.localtime()
print(b)'''

'''def gettime():
    import datetime
    return datetime.datetime.now()
print(gettime())'''

from datetime import datetime
now=datetime.now()
current_time = now.strftime("%H:%M:%S")
print(current_time)

hour=int(now.strftime('%H'))
minute=int(now.strftime('%M'))
second=int(now.strftime('%S'))

if 1<=hour<6:
    print('Hii Dipak Good Night')
elif 6<=hour<12:
    print('hey Dipak Good Morning')
elif 12<=hour<17:
    print('hey Dipak Good Afternoon')
elif 17<=hour<24:
    print('hey Dipak Good Evening')

    












