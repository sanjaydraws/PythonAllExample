

from enum import Enum 

class Color(Enum):
    red =1 
    green =2 
    blue = 3
    

print(Color.red) #Color.red
print(Color(1))#Color.red
print(Color['red']) #Color.red
print(Color.red.value) # 1


# Enums are iterable:

lt = [c for c in Color]
print(lt) # [<Color.red: 1>, <Color.green: 2>, <Color.blue: 3>] 




