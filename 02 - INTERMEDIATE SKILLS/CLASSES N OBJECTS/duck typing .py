#duck test - “If it looks like a duck and quacks like a duck, it’s a duck”
class Vscode:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention check")
        print("Compiling")
        print("Running")


class Laptop:
    def code(self,ide):
        ide.execute()

ide =  MyEditor()
lap1 = Laptop()
lap1.code(ide)


class owner1:
    def car(self):
        print("Audi")
    def bike(self):
        print("BMW")
class owner2:
    def car(self):
        print("Bugatti")
    def bike(self):
        print("BMW")
class owner3:
    def bike(self):
        print("Yamaha")
'''
a=owner1()
b=owner2()
c=owner3()
a.car()
b.car()
c.car()
'''
for i in owner1(),owner2(),owner3():
    i.car()
