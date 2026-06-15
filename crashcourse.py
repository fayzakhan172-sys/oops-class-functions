'''class Factory:
    a = 12 # this is a attribute
    def listen(): # this is a method
        print ("hello")

print (Factory.a) # accessing attribute
Factory.listen() # accesing method'''


'''class Hello:
    a = 12
    def speak(self):
     print (self)
     print ("how are you")

obj = Hello() # created an object
print(obj.a) # object can also access attribute
obj.speak() # when we use objects to call any method 
            # inside class we always send location of my object'''


# constructer
'''class Factory:
    def __init__(self): # constructer function
        print (self)                # whenever a new object is created 
        print ("how are you")# and this self will target the location of your objects
    print ("this is p23 batch")

a = Factory()
b = Factory()
c = Factory()'''

# 2nd use of constructer function

'''class Factory:
    def __init__(self,zips,pockets,materials):
        self.zips = zips
        self.pockets = pockets
        self.materials= materials

    def details(self):
        print ("your bag details are:")
        print (self.zips)
        print (self.Pockets)
        print (self.materials)



reebok= Factory(2,2,"leather")
campus = Factory (4,2,"plastic")

print (campus.materials)'''


'''lass Registration:
    age = 18 # class attribute

    def __init__(self,name,email,age,number):
        if  age >= Registration.age:
            self.name = name # object attribute
            self.email = email
            self.age = age
            self.number = number
        else:
            print ("you can not ragistered you are under age")
            return 
    def details(self):# object method - it targets the location of objects self will take the location of the objects
                           #whichever object is calling 
        print (self.name)
        print (self.email)
        print (self.age)
        print (self.number)

@classmethod
def dummy_details(cls): # class method- it will always access the location of your class
    print (cls.name)
    print (cls.email)
    print (cls.age)
    print (cls.number)


    @staticmethod # static method
    def college_details(): # this method will not target any location 
        print ("I am a very bad collge i will take money and i will not teach you anything that is real world")


student1= Registration("harsh","harsh@mail.com",1234567889)
student1.dummy_details()'''


# inharitance
# one class attribute and methods can be accessed by another class this thing is khown as inharitance
# single level inharitance
'''class BhopalFactory:
    Reg_num = 1647393999300399
    def __init__(self,color,size,type):
        self.color = color
        self.size = size
        self.type = type

    def details(self):
        print ("your shoes details are")
        print (self.color)
        print (self.size)
        print (self.type)

class indorefactory(BhopalFactory):
    def __init__(self, color, size, type, price):
        BhopalFactory.__init__(self,color, size, type)
        self.price = price

shoe1= BhopalFactory("Red",8,"jorden")

shoe2 = indorefactory ("yellow",7,"sneakers",1000)
shoe2.details()
'''

'''# multilevel inheritance

class BhopalFactory:
    Reg_num = 1647393999300399
    def __init__(self,color,size,type):
        self.color = color
        self.size = size
        self.type = type

    def details(self):
        print ("your shoes details are")
        print (self.color)
        print (self.size)
        print (self.type)

class indorefactory(BhopalFactory):
    def __init__(self, color, size, type, price):
        BhopalFactory.__init__(self,color, size, type)
        self.price = price
    
class UjjainFactory(indorefactory):
    def __init__(self,color,size,type,price):
        super().__init__(self,color, size, type)

shoe1= BhopalFactory("Red",8,"jorden")

shoe2 = indorefactory ("yellow",7,"sneakers",1000)
shoe2.details()'''



# multiple inheritanc

# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def details(self):
#         print (self.name)
    
# class Human:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def speak (self):
#         print ("Hello human you speak")

# class Robot(Animal,Human):
#     def __init__(self,name,age):
#         Human.__init__(self,name,age)

# obj1= Robot("Alpha1",2)


# hierarchical inharitance

# hybrid inheritance

'''class Animal:
    pass
class Human:
    pass
class Robots (Animal,Human):
    pass
class AI(Robots):
    pass'''



# polymorphism attribue and method ke bech me ho ta h

'''class Animal:
    name = "lion"
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def detail(self):
        print("the details are")
        print (self.name)
        print (self.age)

class Human:
    name = "Harsh"

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = age

    def detail(self):
        print("the details are")
        print (self.name)
        print (self.age)
        print (self.gender)

obj1 = Animal("giraffe",6)
obj1.display()
obj2 = Human("Harsh",23,"Male")
obj2.display()'''

#  here both the methods are working differently but there names are same thus we are achieving polymorphism





# overridding 
'''class BhopalFactory:
    Reg_num = 1647393999300399
    def __init__(self,color,size,type):
        self.color = color
        self.size = size
        self.type = type

    def details(self):
        print ("your shoes details are")
        print (self.color)
        print (self.size)
        print (self.type)

class indorefactory(BhopalFactory):
    def __init__(self, color, size, type, price):
        BhopalFactory.__init__(self,color, size, type)
        self.price = price

    def details(self):
        return (super().details())
        print (self.price)
    

obj = indorefactory("red",8,"jorden",18000)

obj.details()'''
# this obj can now only call one method that is of indorefactory 
# it can not call bhopal factory detail method
# and this thing is khow as method overidding 



# method overloading = this will not support in pythone baki other languages me support kr tii h

'''class Animal:
    def hello(a):
        pass
    def hello(a,b):
        pass

obj = Animal()
obj.hello(12,45)'''

# same name methods inside a sinlge class but with different parameters this thing is khown as method overloading 
# it is not available in pythone 


# encapsulation  (accesss control and  access modifier)
# protecting the attribute and methods is khow as capculation
# we use access modifier

'''class Animal:
    a = 12 # Public attribute
    _b = 23 # protected attribute
    __c = 45 # private attribute (no one bahar access nhi kr paega )

    def hello (self): # public method
        print ("how are you ")
    def _hello2(self): #protected method
        print ("how are you")

    
    @classmethod @staticmethod
    def __hello3(self): # private method
        print ("how are you 3")

obj = Animal()
print (obj.a)'''



# abstraction (hide the code)

'''from abc import ABC, abctractmethod

class person(ABC):
    @abctractmethod
    def info():
        pass

    @abctractmethod
    def register():
        pass

class Teacher(person):
    def info():
        pass
    def register():
        pass
class students(person):
    def info():
        pass
    def register():
        pass

obj = Teacher()'''

# we have to follow the rules in the abstraction

