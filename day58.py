# Constructors in Python

class person:
    name='Dipak'
    occ='student'

    def info(self):                              #it must requirs self argument
        print(f'{self.name} is a {self.occ}')

a=person()        #This is a new object

print(a.name)



