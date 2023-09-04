# Recursion in python
'''calling a function in that same function '''

def factorial(n):
    if (n==0 or n==1) :
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))
        


# Fibonacci sequence
def Fseq(n):
    if (n==0):
        return 0
    if n==1:
        return 1
    else:
        return (n-1)+(n-2)
    
print(Fseq(10))



    
    

    

