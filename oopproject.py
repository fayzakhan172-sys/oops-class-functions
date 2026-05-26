class students:
    def __init__(self,name,age,email,number):
        self.name = name
        self.age = age
        self.email= email
        self.number = number


    def display_details(self):
        print (self.name)
        print (self.age)
        print (self.email)
        print (self.number)

class class10admission(students):
    def __init__(self, name, age, email, number):
        super().__init__(name, age, email, number)

    print ("addmission successful")


class class12admission(students):
    def __init__(self, name, age, email, number):
        super().__init__(name, age, email, number)
        if self.age >=16:
            print ("admission sucessful")
        else:
            print ("admission failed")

print("press 1 for class 10th admission")
print ("press 2 for class 12th admission")

choice = int (input("enter your choice"))

name = input ("tell your name")
age = int (input("tell your age"))
email= input ("tell your mail")
phone = input ("tell your number")

if choice ==1:
    student1= class10admission(name,age,email,phone)
    student1.display_details()

if choice ==2:
    student1= class12admission(name,age,email,phone)
    student1.display_details()




