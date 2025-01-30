class Base:
    def __init__(self):
        print("Base init")

class A(Base):
    def __init__(self, a_value, *args):
        self.a_value = a_value
        print(f"A {self.a_value}")
        super().__init__(*args)
        print("A init")

class B(Base):
    def __init__(self, b_value, *args):
        self.b_value = b_value
        print(f"B {self.b_value}")
        super().__init__(*args)
        print("B init")

class C(B, A):
    def __init__(self, a_value, b_value):
        super().__init__(a_value, b_value)  #A.__init__() takes 2 positional arguments but 3 were given
        print("C init")

c = C("a_valeur", "b_valeur") 
