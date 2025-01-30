class MyClass:
    def __init__(self):
        self.attribute = 42

obj = MyClass()

def setAttribute(obj, nom, multipler):
    if hasattr(obj, nom):
        setattr(obj, nom,  getattr(obj, nom) * multipler)  

print(hasattr(obj, 'attribute'))

print(getattr(obj, 'attribute'))  
obj.attribute
setattr(obj, 'attribute', 100)  

print(getattr(obj, 'attribute'))
