# dir, __dict__ and help method in Python

#dir()

x=[1,2,3]
print(dir(x))

print(x.__add__)

#__dict__

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p=person('Dipak',22)
print(p.__dict__)    #this will convert the data in dictinory

#help

print(help(person))