'''class Computer:
    def __init__(self,cpu,ram):
        self.ram=ram
        self.cpu=cpu


    def config(self):
        print('Configuration is',self.cpu,self.ram)

com1=Computer('i3',8)
com2=Computer('i5',16)


#Computer.config(com1)
#   Computer.config(com2)

com1.config()  #config will take com1 as an argument 
com2.config()'''



'''class Hello:
    def __init__(self):
        self.name='Jebez'
        self.age=16

    def update(self):
        self.age=19


    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            print('they are different')


p1=Hello()
p1.update()
p2=Hello()



if p1.compare(p2):
    print('They are same')'''


'''class Car:

    wheels=4   #class varivable or static variable

    def __init__(self):
        self.name='Mustang'
        self.mileage=26

c1=Car()
c1.mileage=13
c2=Car()

Car.wheels = 5


print(c1.name,c1.mileage,c1.wheels)

print(c2.name,c2.mileage,c2.wheels)'''




class Student:

    school = 'home ' 

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    #accessor methods 
    def get_m1(self):
        return self.m1
    def set_m1(self,value):
        self.m1=value

    #mutator methods
    @classmethod
    def schoolname(cls):
        return cls.school


    #static method 
    @staticmethod
    def info():
        print('hello guys this is static method')




s1=Student(10,20,30)
s2=Student(40,50,60)

print(s1.avg())
print(s2.avg())

print(s1.schoolname()) #this works normally
print(Student.schoolname()) #we should use @classmethod

Student.info()