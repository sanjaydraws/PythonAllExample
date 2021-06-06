
# Python program to understand the classmethod 


# from datetime import date

# class Person:
#     clsVar = "class var"
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age 


#     # a class method to create a  
#     # Person object by birth year.
#     @classmethod
#     def fromBirthYear(cls, name, year):
#         print(cls.clsVar) # class var
#         return cls(name, date.today().year - year)


#     @staticmethod 
#     def isAdult(age):
#         # print(clsVar) can't access in static method 
#         return age>18 
    
#     def regularMethod(self):
#         print("regular")
#         # print(clsVar) # can't acces  class variable 


# Person1 = Person("chris", 21)
# Person2 = Person.fromBirthYear('chris', 1996)
# # Person1.regularMethod()

# print(Person1.age) #21 
# print(Person2.age) #25
# print(Person2) #<__main__.Person object at 0x01D33CD0>
# print (Person.isAdult(22))  #True 

















# Example2

from PythonAllExample.oop.Example1 import Person


class Student: 
      
    # create a variable 
    name = "Hello World"
      
    # create a function 
    def print_name(obj): 
        print(obj.name) 
    

# create print_name classmethod 
# before creating this line print_name() 
# It can be called only with object not with class

Student.print_name = classmethod(Student.print_name)

# now this method can be called as classmethod 
# print_name() method is called a class method 

Student.print_name()


