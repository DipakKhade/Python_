# super keyword in Python

class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class programmer(Employee):

    def __init__(self,name,id,lang):
        super().__init__(name,id)     #This will add instance present in parent class
        self.lang=lang

e1=Employee('Gaurav',1221)
print(e1.name)

p1=programmer('Dipak',122,'Python')
print(p1.lang)
        

 