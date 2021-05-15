

# Multiple inheritence 

class Base1(object):
    def __init__(self): 
        self.str1 = "Geek1"
        print("Base1") 

class Base2(object): 
    def __init__(self): 
        self.str2 = "Geek2"        
        print("Base2") 

        # d is private instance variable  
        self.__d = 42  

    def fun(self):
        print(self.__d)



class Derived(Base1, Base2): 
    def __init__(self): 
          
        # Calling constructors of Base1 
        # and Base2 classes 
        Base1.__init__(self) 
        Base2.__init__(self) 
        print("Derived") 
          
    def printStrs(self): 
        print(self.str1, self.str2) 


obj = Base2()
obj.fun()
ob = Derived() 

ob.printStrs() 




