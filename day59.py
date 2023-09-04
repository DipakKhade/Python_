# Decorators in Python 



def greet(fx):
    def mfx():        
       print('Good morning')
       fx()
       print('Thanks for using this function')
    return mfx


@greet                      #this will modify the function hello()
def hello():
    print('hello world ')

hello()



# 
def greet(fx):
    def mfx():
        print('My name is')
        fx()
        print('Khade')
    return mfx

@greet
def name():
    print('Dipak')

name()


# 

def greet(fx):
  def mfx(*args, **kwargs):
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mfx

@greet
def hello():
  print("Hello world")

@greet
def add(a, b):
  print(a+b)
  
# greet(hello)()
hello()
# greet(add)(1, 2)
add(1, 2)

 