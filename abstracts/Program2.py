# Concrete Methods in Abstract Base Classes : 
# Concrete classes contain only concrete (normal)methods whereas abstract classes may contain both concrete methods and abstract methods.
#  The concrete class provides an implementation of abstract methods,
#  the abstract base class can also provide an implementation by invoking the methods via super(). 

import abc 
from abc import ABC , abstractmethod 

class R(ABC):

    # concreate method 
    def rk(self):
        print("Abstract base class ")

class K(R):
    def rk(self):
        super().rk()
        print("sub class")  

r = R()
r.rk() # Abstract base class 
r = K()
r.rk()
