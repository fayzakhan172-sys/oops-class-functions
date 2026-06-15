#Abstractmethod
'''
from abc import ABC, abstractmethod

class shapes(ABC):

    @abstractmethod
    def area():
        pass

    @abstractmethod
    def perimeter():
        pass

class Square(shapes):
    def __init__(self,side):
        self.side = side

    def perimeter(self):
        print (4 * self.side)

    def area (self):
        print (self.side * self.side)

class circle (shapes):
    def __init__(self,radius):
        self.radius = radius

    def area():
        pass

    def  perimeter():
        pass

obj = Square(10)'''


'''class Robots:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"hello my name is {self.name}"

obj = Robots("alpha1")
obj2= Robots("beta1")

print (obj)
print (obj2)'''
 #dunder method

'''class numbers:
    def __init__(self,value):
        self.value = value

    def __add__(self,other):
        return self.value + other .value
    
    def __eq__(self,value):
        return self.value == value.value


a = numbers (20)
b = numbers (30)

print (a==b)'''

a = 12 
print (type(a))







