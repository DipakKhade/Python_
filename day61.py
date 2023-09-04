# Inheritance in Python 

class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showDetails(self):
            print(f'The name of employee is :{self.id} is {self.name}')


#creating class with arrgument class
class programmer(employee):
     def showlanguage(self):
        print('The deafult language is Python')

e1=programmer('Dipkak',2203256)
e2=programmer('Gaurav',1234456)




# e1=employee('Dipak',214)
# e1.showDetails()

# e2=employee('Gaurav',117)
# e2.showDetails()



         