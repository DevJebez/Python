'''class Student:
    def __init__(self,name,rollno):
    	self.name = name
    	self.rollno = rollno
    	self.lap = self.Laptop()
    def show(self):
    	print(self.name,self.rollno)
    	self.lap.show()

    class Laptop:
    	def __init__(self):
    		self.brand='Hp'
    		self.cpu='i5'
    		self.ram=16
    	def show(self):
    		print(self.brand,self.cpu, self.ram)

s1=Student('jebez',13)
s2=Student('oswald',14)


s1.show()
'''


#INHERITANCE
class A:
	def __init__(self):
		print("In init A ")
	def feature1(self):
		print('feature 1 is working')
	def feature2(self):
		print('feature 2 is working')

class B(A):
	def __init__(self):
		print('in init B')
		super().__init__()
	def feature3(self):
		print('feature 3 is working')
	def feature4(self):
		print('feature 4 is working')

  # Class D also inherited the constructor of class A since class D doen't have its own constructor


class C: 
	def __init__(self):
		print('in init C')
	def feature5(self):
		print('feature 5 is working')
  
class D:
    def __init__(self):
    	print("In init D")
    def feature6(self):
    	print('feature6 is working')

class E(C,D):
	def __init__(self):
		super().__init__() #This calls the instructor in the order of MRO (left to right)
		print('In in init E')
	def feature7(self):
		print('feature 7 is working')
a1=C()

