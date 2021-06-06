# By defining an abstract base class, you can define a common Application Program Interface(API) for a set of subclasses. 
#  Python does not provide abstract classes. Python comes with a module that provides the base for defining Abstract Base classes(ABC) and that module name is ABC

from abc import ABC , abstractmethod 

class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass 

class Triangle(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")
    

class Pentagon(Polygon): 
    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")

class Hexagon(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")

class Quadrilateral(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")

R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides() 

R = Pentagon()
R.noofsides()