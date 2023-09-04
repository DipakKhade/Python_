# Multiple Inheritance in Python | Python Tutorial - Day #79

class Coder:
    def __init__ (self,name):
        self.name=name

    

class Statistician:
    def __init__(self,lang):
        self.lang=lang

    
class CoderStatistician(Statistician,Coder):
    def __init__ (self,name,lang):
        self.name=name
        self.lang=lang

d=CoderStatistician('Dipak','pyhton')
print(d.name)
print(d.lang)

# mro    (Method resolution Order)
print(CoderStatistician.mro())




