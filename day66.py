# Instance variables vs Class variables in Python 

class Employee:
    company_name="Apple"        #This is a class variable
    noOfEmployee=0
    noOfEmployee +=1        #The no is increased as the no of employee is emp increased
    def __init__(self,name):
        self.name=name            #This is a instance variable
        self.raise_amount=0.02
         
    def showDetails(self):
        print(f'The name of employee is {self.name} and the raise amount in {self.company_name} is {self.raise_amount}')
        print(f'no of employee is {Employee.noOfEmployee}')


emp1=Employee('Dipak')
emp1.showDetails()             
# Employee.showDetails(emp1)    #This is a same as above statement

emp2=Employee('Gaurav')
emp2.showDetails()
