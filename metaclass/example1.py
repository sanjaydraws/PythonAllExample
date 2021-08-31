# everything in python is object 


# class Test:
#     pass

# print(type(Test()))  # <class '__main__.Test'>
# print(type(2)) #<class 'int'>

# ==================

class Foo:
    def show(self):
        print("Hello World")


def add_attribute(self):
    self.z = 90 

# creating Test class 
# Test = type('Test',() , {"x":5} )

# to inherit Foo class  
Test = type('Test', (Foo,), {"x" : 5, "add_attribute":add_attribute})

t = Test()
t.y = "Hello"
print(t.x) #5 
print(t.y)  #Hello 
t.show() # Hello World

t.add_attribute() # to add atribute 
print(t.z) # 90

# =================================================
