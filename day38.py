## Raising custom errors in python

#we use raise keyword to raise custon error


# a=int(input('Enter the number between 5 to 9 : '))
# if a<5 or a>9:
#     raise ValueError('Enter the number between 5 to 9')



#Quick quiz

a=input('Enter the string : ')

if a=='quit':
    raise ValueError('Enter word other then "quit"')
else:
    print(f'your entered word is : {a}')


 
  