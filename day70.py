# Class Methods as Alternative Constructors in Python 
'''
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=21


e=person('Dipak',21)
print(e.name)
print(e.age)

#passing arrguments by spliting the string
string='Gaurav-21' 
p1=person(string.split('-')[0],string.split('-')[1])
print(e.name)
print(e.age)  '''


###we pass these parameters by by using class methods as an Alternative constructors

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

#by using class methods as alternative constructors

    @classmethod
    def fromstr(cls,string):
        return cls(string.split('-')[0],int(string.split('-')[1]))


string='Gaurav-22'
p2=person.fromstr(string)
print(p2.name)
print(p2.age)

   