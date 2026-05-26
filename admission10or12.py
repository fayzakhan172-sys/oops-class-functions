'''class sharmavishnu: # blueprint of object we can call its a class
    def sample():
        print ('this is sample function')

    def sample2():
        print ("this is sample2 functtion")
sharmavishnu.sample()
sharmavishnu.sample2()

class sharmavishnu:
    a = "jojo" # class ke andr ke function -> method
    def sample(): # class ke andr ke function->method
        print ("this is sample function")
sharmavishnu.sample()
print(sharmavishnu.a)'''



# class Animal:
#     #Attribute
#     name ="Animal"

#     #Method
#     def greet(self): # jb bhi class ke andr function ko object ke help se call kro ge toh ek parameter set ho jae ga
#         print ('This is Animal class')

# # onject ke naam same as hota hai as name of the variable
# tau = Animal() # here tau is object
# tau.greet()
# print (tau.name)


# create a class which will perform two task 
# 1> greet the user-"this is class"
# 2> adding up two numbers

'''class baggha:
    def greet(self):
        print('hello from baggha')
    def add(self):
        a= 10
        b=10
        print (a+b)

obj = baggha()
obj.greet()
obj.add()'''

# Constructer -> represent by __init__ (dunder methods)
# constructer sabse phele execute hone wale funstions hai doesnt matter inke upar ya neeche koi function present hai
# class sharmavishnu:

#     def __init__(self,name,age):
#         self.name = name # instance attribute
#         self.age = age
#         print ('This is constructer function')

#     def manu(self):
#         print (self.name)
#         print (self.age)
#         print ('paneer khulche')

# obj = sharmavishnu("amit",21) 
# obj.manu()


# make a class which will take 2 numbers as input create
# 1. 2 instance attribute
# 2. create a function which will print greatest among them

# class sample:
#     def __init__(self,a,b):
#         self.a= a
#         self.b= b
    
#     def greater (self):
#         if self.a > self.b:
#             print (self.a, 'is bada')
#         else:
#             print(self.b,"chhota")
# obj = sample (10,20)
# obj.greater()



