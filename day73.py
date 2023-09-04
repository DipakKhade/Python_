# Magic/Dunder Methods in Python | Python Tutorial - Day #73

class Employee:
    name='Dipak'
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
            return i
        
    def __str__():
        print(f'The name of the employee is{Employee.name} ')

e=Employee()
print(e.name)
print(len(e))



