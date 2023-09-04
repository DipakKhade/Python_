# Exercise 5 - Snake Water Gun


import random
options=['snake','water','gun']
computer=str(random.sample(options,1))

user=input('select : snake/water/gun ')

# By using if else
if computer==user:
    print('Draw')

# Loss
elif computer=='snake' and user=='water':
    print('You loss  ')
elif computer=='water' and user=='gun':
    print('You loss  ')
elif computer=='gun' and user=='snake':
    print('You loss  ')

# Win
elif computer=='snake' and user=='gun':
    print('You win  ')
elif computer=='water' and user=='snake':
    print('You win  ')
elif computer=='gun' and user=='water':
    print('You win  ')


