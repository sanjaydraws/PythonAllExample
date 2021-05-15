class Person:

    x = "class variable for every object"
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def mufunc(self):
        print("Hello my name is ", self.name)


p1 = Person("John", 34)
p2 = Person("Chris", 12)
print(p1.name) 
print(p1.x) #      "class variable for every object"
print(Person.x) #class variable for every object
print(p2.x) #class variable for every object


# modify 
p1.name = 90
print(p1.name)

# Delete Object Properties
# del p1.name
# print(p1.name) # AttributeError: 'Person' object has no attribute 'name'


# del p1 # delete objects
# print(p1) # NameError: name 'p1' is not defined



# class has no definition
# class Person:
#     pass 
















