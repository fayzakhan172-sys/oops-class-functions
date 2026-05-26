# INHARITANCE
'''
1.single Inheritance # parent class and 1 child 
2.multiple Inheritance  # 2 parent 1 child
3.multilevel Inheritance # one child becomes parent
4.hierarchial Inheritance # one parentmultiple child
5. Hybrid Inheritance

'''

# inharitance 

'''class parent:

    def __init__(self):
        print ("this is constructer")
    def greet(self):
        print('this is parent class')

class child (parent):
    def __init__(self):
        print ("this is child class constructer")
    def show(self):
        print("this is child class")

obj = child()
obj.greet()
obj.show()'''

# single Inharetance
# class Factory:
#     def __init__(self,name,color):
#         self.name= name
#         self.color= color
#     def show(self):
#         print(f"Bag has {self.name} and {self.color} color")

# class Bata(Factory):
#     def __init__(self,name,color,zip,pockets):
#         super().__init__(name,color)
#         self.zip = zip
#         self.pockets = pockets

#     def display (self):
#      print(f'Bag has {self.name} , {self.color} color , {self.zip} zip and {self.pockets} pockets')
# Rahul = Bata('Rahul','Purple',4,10)
# Rahul.display()
    




# 2 Multiple inharitance ->2 parent , 1 child

# class Father: # parent1

#     def __init__(self):
#         print ("this is father class constructer")

#     def greet_father(self):
#         print ("this is father class")

# class Mother:  # parent2
#     def __init__(self):
#         print("This is mother class constructer")

#     def greet_mother(self):
#         print("this is Mother class")

# class child(Mother,Father): # child class
#     # if we have to run constructer of father class first
#     def __init__(self):
#         Father.__init__(self) # sabse phele father constructer will be run
#         Mother.__init__(self) # after father class mother class constructer will be run 

# obj = child()
# obj.greet_father()
# obj.greet_mother()

#Multilevel Inheritance

# class A: #super parent 
#     def greet(self):
#          print ("this is class A")

# class B (A): # child class
#     def show(self):
#         print("This is class B")
    
# class c(B):
#     def details(self):
#         print ("this is class C")

# obj = c()
# obj.show()
# obj.greet()




# class CEO: # super parent
#     def __init__(self):
#         print ("This is CEO class constructer")

# class Manager (CEO): # child class
#     def __init__(self):
#         super().__init__()
#         print("This is Manager class constructor")

# class Employee(Manager): # child 
#     def __init__(self):
#         super().init__()
#         print ("This is Employee class constructor")

# rahul= Employee()




# hierarchial Inheritance
'''class Parent:
    def greet(self):
        print ("This is parent class")

class child1(Parent):
    pass

class child2(Parent):
    pass

obj = child2()
obj.greet()

obj2 = child1()
obj2.greet()'''




class Account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def details (self):
        print (f"Hello {self.name} you have {self.balance}")

class saving (Account):
    def __init__(self,name,balance):
        super().__init__(name,balance)
        print (f"This is saving class constructor {self.name}, {self.balance}")

class current (Account):
    def __init__(self,name,balance,type):
        super().__init__(name,balance)
        self.type = type
        print (f"this is current class constructer {self.name}, {self.balance}, {self.type}")

obj = current ("mukesh",0,"current")