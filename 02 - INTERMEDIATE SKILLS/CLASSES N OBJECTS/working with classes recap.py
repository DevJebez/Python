'''

class Computer: # class - a blue print of the object
    def __init__(self,cpu,ram): # special method
        print("in init")
        self.cpu=cpu  # here self is the object which is com1 and com2
        self.ram=ram
        
    def config(self): #every computer has some confing rt :>
        print("Config is",self.cpu,self.ram)



# let's say a= 5 now the type of a is integer
# now what's the type of com1 so we assign Computer() ( so thats the type)
#This gives the object of computer to com1

com1 =  Computer("i5",8)  # by default it is taken as (object,arg1, arg2), IT JUST intitalizes the object
com2 = Computer("Ryzen 3",16)

#let's chk the type of com1

#print(type(com1)) #<class '__main__.Computer'>


#let's call the function which is inside the class


Computer.config(com1) #every object has its own behaviour
Computer.config(com2)



#alternate method
com1.config()  # behind the scenes the config will take com1 as argument #this will print the config
com2.config()

'''

'''
class student():
    def __init__(self):
        self.name="Jebez"
        self.age=18
    def update(self):
        self.age=25
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False
        
s1=student()
s2=student()

s2.update()

if s1.compare(s2):
    print("They are same")
else:
    print("They are different")


print(s1.name)
print(s2.name)



'''


'''
import math 

class student():
    
    school="PVM"
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()
    def show(self): # a method with instance variables in it is called as instance method
        print("Name:",self.name)
        print("ROll no:",self.rollno)
        self.lap.show()
        
    @classmethod  # this method bound to object than class
    def get_schl(cls):
        return cls.school

    @staticmethod
    def info(): # this method has nothing to do with the class 
        print("Welcome to PVM")

    class Laptop():
        def __init__(self):
            self.brand="Lenova"
            self.cpu="i5"
            self.ram='8'
        def show(self):
            print("Brand :",self.brand)
            print("CPU :",self.cpu)
            print("RAM :",self.ram)

n1=input("Enter your name:")
r1=int(input("Enter your rollno:"))
s1=student(n1,r1)

student.info()
s1.show()

'''

'''
class cars:
    def __init__(self,cc,brand,model):
        self.cc=cc
        self.brand=brand
        self.model=model
        self.own=self.owner()
    def spec(self):
        print("CC : ",self.cc)
        print("BRAND : ",self.brand)
        print("MODEL :",self.model)
        self.own.spec()
    class owner:
        def __init__(self):
            self.name = "Jebez"
            self.gmail = "jebez@gamil.com"
        def spec(self):
            print(self.name,"\n",self.gmail)

car1 = cars(10000,"mustang","Dodge challenger")
car2 = cars(11000,"BMW","BMW X7")

car1.spec()
'''


class A:
    a=400
    def __init__(self):
        print("In A init")
    def feature1(self):
        print("Feature 1-A is working ")
    def feature2(self):
        print("Feature 1 is working ")
    @classmethod
    def jeez(cls):
        print("I'm a class method of A man!")
class B:
    def __init__(self):
        print("In B init ")
        super().__init__() #we are trying to call init of A 
        
    def feature1(self):
        print("Feature 1 -B is working ")
    def feature4(self):
        print("Feature 4 is working ")
class C(B,A):
    def __init__(self):
        print("in C init")
c= C()
c.feature1()
