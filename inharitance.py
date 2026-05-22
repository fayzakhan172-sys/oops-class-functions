# INHARITANCE
'''
1.single Inheritance # parent class and 1 child 
2.multiple Inheritance 
3.multilevel Inheritance
4.hierarchial Inheritance
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


class Factory:
    def __init__(self,name,color):
        self.name= name
        self.color= color
    def show(self):
        print(f"Bag has {self.name} and {self.color} color")

class Bata(Factory):
    def __init__(self,name,color,zip,pockets):
        super().__init__(name,color)
        self.zip = zip
        self.pockets = pockets

def display (self):
    print 




# 2 Multiple inharitance ->2 pafrent , 1 child

class Father: # parent1

    def __init__(self):
        print ("this is father class constructer")

    def greet_father(self):
        print ("this is father class")

class Mother:  # parent2
    def __init__(self):
        print("This is mother class constructer")

    def greet_mother(self):
        print("this is Mother class")

class child(Mother,Father): # child class
    # if we have to run constructer of father class first
    def __init__(self):
        Father.__init__(self) # sabse phele father constructer will be run
        Mother.__init__(self) # after father class mother class constructer will be run 

obj = child()
obj.greet_father()
obj.greet_mother()



