# Abstract Properties : 
# Abstract classes include attributes in addition to methods, you can require the attributes  in concrete classes by defining them with @abstractproperty. 

# Python program showing
# abstract properties
 
import abc
from abc import ABC, abstractmethod
 
class parent(ABC):
    @abc.abstractproperty
    def geeks(self):
        return "parent class"
class child(parent):
      
    @property
    def geeks(self):
        return "child class"
  
  
try:
    r =parent()
    print( r.geeks)
except Exception as err:
    print (err)
  
r = child()
print (r.geeks)