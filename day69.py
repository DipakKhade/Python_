# Class Methods in Python 

class Employee:
    company='Apple'
    def show(self):
        # name='Dipak'
        print(f'The name is {self.name} and the company is {self.company}')


    @classmethod         #decorator
    def changecompany(cls,newcompany):
        cls.company=newcompany


e1=Employee()
e1.name='Dipak'
e1.show()

e1.company='Tesla'
e1.show()





        
    