# Exception handling

a=input('Enter the number : ')

print(f'The multiplication table of {a} is :')

try:
        for i in range(1,11):
                print(f'{a}*{i} = ', int(a)*i)

except Exception as e:
        print(e)

print('the end of program')



#.

a=input('Enter the number : ')

print(f'The multiplication table of {a} is :')

try:
        for i in range(1,11):
                print(f'{a}*{i} = ', int(a)*i)

except:
        print('invalid input !')

print('the end of program')
        
#we can use multiple except 
#we also overtake some specific error



