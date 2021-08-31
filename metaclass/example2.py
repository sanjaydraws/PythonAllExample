
# inherit type class to create Meta 
class Meta(type):
    # this is always called 
    def __new__(self, class_name, bases,attr):
        print(attr)
        return type(class_name, bases,attr)


class Dog(metaclass =Meta):
    x =5 
    y = 9 

    def Hello(self):
        print("Helldsdo ")


    



