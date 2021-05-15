class Person:
    
    x =45
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        

    @classmethod
    def  fun1(cls):
        print(cls.x)
        # print(cls.name) # can't access instance variable


    @staticmethod
    def fun2():
        print("Hello fun")





p1 =  Person('chris',45)
# p1.fun1()
Person.fun1()
Person.fun2() # Hello fun 
p1.fun2()








