# Exercise 2: Solution & Shoutouts | Python Tutorial - Day #26

'''from datetime import datetime

now=datetime.now()
c_time=now.strftime("%H")
print(c_time)'''



# pre solved exercise in day 15

from datetime import datetime
now=datetime.now()
current_time = now.strftime("%H:%M:%S")
print(current_time)

hour=int(now.strftime('%H'))         #coverting a hour in int
# minute=int(now.strftime('%M'))
# second=int(now.strftime('%S'))

if 1<=hour<6:
    print('Hii Dipak Good Night')
elif 6<=hour<12:
    print('hey Dipak Good Morning')
elif 12<=hour<17:
    print('hey Dipak Good Afternoon')
elif 17<=hour<24:
    print('hey Dipak Good Evening')
