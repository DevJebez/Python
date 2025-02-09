
class Cat:
    def __init__(self):
        print("Hello I'm a cat ")
    def meow(self):
        print("Meoow meoow")
    def eat(self):
        print("Eating")
class Animal(Cat):
    def eat(self):
        print("Eating :>")
        
a = Cat()
b = Animal()
a.eat()
b.eat()