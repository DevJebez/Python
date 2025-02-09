print("Welcome to method overloading")
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1 
        self.m2 = m2
    def sum(self,*args):
        s=0
        for i in args:
            s+=i
        return s
g=Student(58,59)

print(g.sum(4,6))


