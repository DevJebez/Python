'''
a=4
c=6
print(a+c)
print(int.__add__(a,c))  #behind the scene of + operator 


class Student:
	def __init__(self,m1,m2):
		self.m1=m1
		self.m2=m2
	def __add__(self,b):
		m1=self.m1+b.m1
		m2=self.m2+b.m2
		s3=Student(m1,m2)
		return s3
	def __gt__(self,other):
		a=self.m1+other.m1
		b=self.m2+other.m2
		if a>b:
			return True
		else:
			return False	

	def __str__(self):
		return '{} {}'.format(self.m1,self.m2)

s1=Student(100,90)
s2=Student(90,50)
s3=s1+s2
print(s3.m1)  
 

if s1>s2:
	print('s1 wins')
else:
	print('s2 wins')
print(s1)
print(int(a.__str__()))#behind the scenes the a.__str__()


a=5
b=1
print(a+b)
print(int.__add__(a,b))# behind the scene 

c="hello"
d="World"
print(str.__add__(c,d)) 
'''
class Student:
	def __init__(self,m1,m2):
		self.m1 = m1
		self.m2 = m2
	def __add__(self,other):
		m1=self.m1+ other.m1
		m2= self.m2+other.m2
		s3 =  Student(m1,m2)
		return s3
	def __gt__(self,other):
		r1=self.m1 + self.m2
		r2 = other.m1 + other.m2
		if r1 > r2 : 
			return True
		else :
			return False
	def __str__(self):
		return '{} {}'.format(self.m1,self.m2)

s1=Student(90,55)
s2=Student(94,95)

s3 = s1 + s2 # --> Student.__add__(s1,s2)
if s1 > s2:
	print("s1 wins")
else:
	print("s2 wins")


print(s3) # behind the scene it works as print(s3.__str__())
print(s2)
print(s1)


class MyClass:
	def __init__(self, value):
		self.value = value

	def __and__(self, other):
		return MyClass(self.value and other.value)
	def __str__(self):
		return self.value

a = MyClass(True)
b = MyClass(False)
c = a & b # c.value is False
print(c.__str__())

