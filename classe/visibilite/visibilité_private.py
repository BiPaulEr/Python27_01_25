class Secret:
    def __init__(self):
        self.__secret = "Not so secret"
        self.__private_method() 

    def __private_method(self):
        print("Private method called")

    def reveal_secret(self):
        print(self.__secret) 


obj = Secret()
#print(obj.__secret)  # 'Secret' object has no attribute '__secret'

#print(obj.__private_method())  

print(obj._Secret__secret)  
print(obj._Secret__private_method()) 
