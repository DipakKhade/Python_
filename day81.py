# Hybrid and Hierarchical Inheritance in Python | Python Tutorial - Day #81

# Hybrid inheritance example
class BaseClass:
    pass

class Derivedclass1(BaseClass):
    pass

class DerivedClass2(BaseClass):
    pass

class DerivedClass3(Derivedclass1,DerivedClass2):
    pass


# hierarchical inheritance
class BaseClass:
    pass

class D1(BaseClass):
    pass

class D2(BaseClass):
    pass

class D3(D1):
    pass


