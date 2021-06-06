class Person:
    """A simple class.""" # docstring
    x = "class variable for every object" # class atribute 
    def __init__(self, name, age):
        """this is initializer special method """
        self.name = name
        self.age = age  # instance attribute 

    def __str__(self): # special method 
        return self.name 

    def mufunc(self): # regular method 
        print("Hello my name is ", self.name)


p1 = Person("John", 34)
p2 = Person("Chris", 12)
# print(p1.name)  #John 

# acces class variable using object or class 
# print(p1.x) #      "class variable for every object"
# print(Person.x) #class variable for every object


# modify 
# p1.name = 90 # string to int can be converted 
# p1.name ="Jonhn"
# print(p1.name)


#change class variable value using object doesn't change value
p1.x = 34 
print(p2.x) #class variable for every object
print(p1.x) # 34 
print(Person.x) # #class variable for every object

# class variable value can be changed using class name
# Person.x = 34 
# print(p2.x) # 34


# Delete Object Properties
# del p1.name
# print(p1.name) # AttributeError: 'Person' object has no attribute 'name'


# del p1 # delete objects
# print(p1) # NameError: name 'p1' is not defined


print( p1.__str__())



# class has no definition
# class Person:
#     pass 
















