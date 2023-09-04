# Method Overriding in python

# we can override the methids in class

class shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def area(self):
        return self.x*self.y
    
rec=shape(5,6)
print(rec.area())




