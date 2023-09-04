# Exercise 4  : solution

mystr=input('Enter the massage : ')

coading=True
if coading:

   length=len(mystr)

   if length<3:
    print(mystr[::-1])
   else:
    print('abc'+mystr[1:len(mystr)]+mystr[0]+'xyz')

