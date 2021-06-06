
# In this case, "monkey patching" means adding a new variable or method to a class after it's been defined. For
# instance,
class A(object):
    def __init__(self, num):
        self.num = num 
    
    def __add__(self, other):
        return A(self.num + other.num) 



def get_num(self):
    return self.num 

# add this as a method in A
# functions are objects just like any other object, and methods are functions that
# belong to the class.
# function get_num shall be available to all existing (already created) as well to the new instances of A

foo = A(42)
A.get_num = get_num 

bar  = A(5)
print(foo.get_num()) #42 
print(bar.get_num())#5

