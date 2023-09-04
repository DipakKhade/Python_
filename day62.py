# Access Modifiers in Python 

# by deafult every variable is public in python

class employee:
    def __init__(self):
        self.name='Dipak'

a=employee()        
print(a.name)            #variable is accessible 


class employee:
    def __init__(self):
        self.__name='Dipak'

a=employee()        
# print(a.__name)    #this indicates the private    but it still can be accessible



#to access indirctly
class employee:
    def __init__(self):
        self.__name='Dipak'

a=employee()        
print(a._employee__name)    




