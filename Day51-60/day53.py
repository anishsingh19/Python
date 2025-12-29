#Day53 - Map_Filter and Reduce in Python 
#built-in functions that allow to apply a funtion to a sequence of elements
#and return a new sequence. known as higher-order functions, as they take 
#other functions as arguments. 

def cube(x):
    return x*x*x
print(cube(2))

l = [1,2,4,6,4,3]
newl = []
for item in l:
    newl.append(cube(item))
print(newl)


print("Map function")
# map(function, iterable)
#funtion argument is a funtion that is applied to each 
#element in the iterable object.
newl2 = map(cube, l)
print(newl2)
newl3 = list(map(cube, l))
print(newl3)
newl4 = list(map(lambda x: x*x*x, l))
print(newl4)


print("Filter function")
# filter(predicate, iterable)
#predicate argument is a function that returns a boolean value and is 
#applied to each element in the iterable argument. 
def filter_function(a):
    return a>4

filterl = filter(filter_function, l)
print(filterl)
filterl = list(filter(filter_function, l))
print(filterl)


print("Reduce Function")
#reduce(function, iterable)
#reduce function applies the function to the first two elements 
# in the iterable and the applies the function to the result and 
# the next element, and so on.
from functools import reduce

numbers = [1,2,3,4,5]
# numbers = [3,3, 4,5]   #Working of reduce function
# numbers = [6,4, 5]
# numbers = [10,5]

sum = reduce(lambda x, y: x+y, numbers)

print(sum)




















