# Local vs Global Variables

x=18           #Global 
print(x)

def my_function():
    global x
    x=7          #Local
    print(x)    
    print('Hey i am  Dipak')

my_function()


