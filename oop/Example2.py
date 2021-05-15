
# Python program to understand the classmethod 


from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 


    # a class method to create a  
    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)


    @staticmethod 
    def isAdult(age):
        return age>18 

Person1 = Person("chris", 21)
Person2 = Person.fromBirthYear('chris', 1996)

print(Person1.age)
print(Person2.age)
print(Person2)
print (Person.isAdult(22)) 
















# Example2

# class Student: 
      
#     # create a variable 
#     name = "Hello World"
      
#     # create a function 
#     def print_name(obj): 
#         print(obj.name) 
    

# # create print_name classmethod 
# # before creating this line print_name() 
# # It can be called only with object not with class

# Student.print_name = classmethod(Student.print_name)

# # now this method can be called as classmethod 
# # print_name() method is called a class method 

# Student.print_name()


