
# def cube(y): 
#     return y*y*y 

# lambdacube = lambda y : y*y*y 


# print(lambdacube(3))



# from typing import final


from typing import final


li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 

# final_list = list(filter(lambda x: (x %2 != 0 ) , li))

# print(final_list) 



# final_list = list(map(lambda x : x *2, li))

# print(final_list)


# animals = ['dog', 'cat', 'parrot', 'rabbit'] 


# upper_animal = list(map(lambda animal : str.upper(animal), animals))

# print(upper_animal)



# from functools import reduce 

# li = [5, 8, 10, 20, 50, 100] 
# sum = reduce((lambda x,y : x + y), li)
# print(sum)


import functools 

lis = [ 1 , 3, 5, 6, 2, ]  

print ("The maximum element of the list is : ",end="")  

print(functools.reduce(lambda a,b : a if a >b else b, lis))

