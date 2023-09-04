# Lambda functions in Python

# def double(x):
#     return x*2

# print(double(2))



#the abouve function using lambda function

# double=lambda x:x*2

# print(double(2))



# passing function as a argument
def add(fx,value):
    return fx(value)+2

print(add(double,2))

# OR

def add(fx,value):
    return fx(value)+2

print(add(lambda x:x*2,2))        #The anonimus function i.e we pass that function as an argument but it does not have a name




