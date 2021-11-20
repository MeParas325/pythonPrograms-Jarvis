# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type="Rectangle"
    sides=4

    def __init__(self):
        self.length=3
        self.breath=2

    def printarea(self):
        return self.length * self.breath

rect=Rectangle()
print(rect.printarea())
# emp=Shape()  #Error