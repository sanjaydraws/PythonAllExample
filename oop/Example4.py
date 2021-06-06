# inheritence 

class Person(object): 
       
    def __init__(self, name, idnumber):    
                self.name = name 
                self.idnumber = idnumber 
    
    def display(self): 
                print(self.name )
                print() 
                print(self.idnumber) 


class Employee(Person):
   def __init__(self, name, idnumber, salary, post): 
                self.salary = salary 
                self.post = post
                 # invoking the __init__ of the parent class  
                Person.__init__(self, name, idnumber)   



# creation of an object variable or an instance 
e = Employee('Rahul', 886012, 200000, "Intern")     
  
# calling a function of the class Person using its instance 
e.display() 

# Built in function 
# True if DerivedClass is a subclass of the BaseClass
print(issubclass(Employee, Person))  #True 
print(isinstance(e, Employee)) #True 
print(type(e)) # <class '__main__.Employee'>


