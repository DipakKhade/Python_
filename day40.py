# Exercise 4 - secret code language

mystr=input('Enter the massage : ')

length=len(mystr)

if length<3:
    print(mystr[::-1])
else:
    print('abc'+mystr[1:len(mystr)]+mystr[0]+'xyz')


