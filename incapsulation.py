# incapsulation
'''class Animal:
    name= "lion"# public attribute
    _age = 12 # protected attribute
    __height = 120 # private attribute

    @classmethod
    def speak (self): # public object method
        print ("the lion roars")

    def _walk(self): # protected object method
        print ("the lion is walking")

    def __sleep(self): # private ,method
        print ("the lion is sleeping")

obj1= Animal()
# print (obj1.__height)
obj1.__sleep()'''

# private attributes and methode can not be accessed by 
# your object and inherited classes

# polynorphism
'''class Animal:
    def speak(self):
        print ("animals are shouting")

class Human:
    def speak(self):
        print ("humans are intelligent so they are speacking")

obj1= Animal()
obj2=Human ()

obj1.speak()
obj2.speak()'''
# both the speak methods appears to be 
# same but both have different task and this is
# khown as polymorphism 

# method overridding

class Reebok:
    def __init__(self,material,size):
        self.material = material
        self.size = size

    def details (self):
        print ("your bag detail is :")
        print (self.material)
        print (self.size)

class campus(Reebok):
    def __init__(self, material, size,color):
        super().__init__(material, size)
        self.color= color

    def details(self):
        print (self.color)
        print (super().details())

obj1 = campus("leather",10,'black')
obj1.details()

# a child class object has the power to call methods and attributes of a parent class but he can not call the details 
# method of his parent class cause that details methods  is overriden and this concept is khown as method overriding


# overloading 
class animal:
     def hello(self,a):
         print ("how are you")

     def hello (self,a,b):
         print ("how are you man")

# method overloading iis a concept  where are you define similar name methods inside a single class with different parameters