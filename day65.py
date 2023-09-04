# Static Methods in Python

class Math:
    def __init__(self,num):
        self.num=num

    def addtonum(self,n):
        self.num=self.num+n

    @staticmethod
    def add(a,b):
        return a+b

a=Math(5)
a.addtonum(6)
print(a.num)


# it is callable
print(a.add(2,3))
# or
print(Math.add(18,7))

