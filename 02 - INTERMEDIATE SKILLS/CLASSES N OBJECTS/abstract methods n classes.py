from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def wheels(self):
        pass
    @abstractmethod
    def seats(self):
        pass
class Bugatti(Car):
    def wheels(self):
        print("Bugatti has four wheels")
class BMW(Car):
    def seats(self):
        print("2 seats ")
o1 = BMW()
o1.seats()