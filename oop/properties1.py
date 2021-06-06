
# Python classes support properties, which look like regular object variables, but with the possibility of attaching
# custom behavior and documentation

from typing import NewType


class MyClass(object):
    def __init__(self):
        self._my_string = ""
    
    @property 
    def string(self):
        """A profoundly important string."""
        return self._my_string 

    @string.setter 
    def string(self, new_value):
        assert isinstance(new_value, str), "Give me a string not a %r!" %type(new_value)
        self._my_string = new_value

    @string.deleter
    def x(self):
        self._my_string = None 

mc = MyClass()
mc.string = "String!"
print(mc.string)
# del mc.string 

# As well as the useful syntax as above, the property syntax allows for validation, or other augmentations to be added
# to those attributes. This could be especially useful with public APIs - where a level of help should be given to the
# user.