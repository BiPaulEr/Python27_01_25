class MyClass:
    def __init__(self):
        self.attribute = 42

myClass = MyClass()

class DerivedClass(MyClass):
    pass

derivedClass = DerivedClass()

print(isinstance(derivedClass, MyClass))

print(isinstance(derivedClass, DerivedClass))