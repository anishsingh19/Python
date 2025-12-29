#Day59 - Decorators in Python 

# - Python decorators are a powerful and versatile tool that allow you to 
# modify the behavior of functions and methods. 
# - They are a way to extend the functionality of a function or method 
# without modifying its source code.
# - A decorator is a funtion that takes another function as an argument and 
# returns a new function that modifies the behavior of the original function.
# - The new function is often reffered to as a "decorated" function. 
# - The basic syntax for using a decorator is the following: 

# @decorator_function
# def my_function():
#     pass 

# The @decorator_function notation is just a shorthand for the following code: 
# def my_function():
#     pass 
# my_function = decorator_function(my_function)

#Decorators are often used to add functionality to functions and methods, such 
# logging, memoization and access control. 


                          
def greet(fx):                      #greet function takes function as an input
    def mfx(*args, **kwargs):       #mfx: modify fx   (*args, **kwargs are used to solve
         # *args takes arguments as tuple               # add function's argument issue)
         # **kwargs takes arguments as dictionary         
        print("Good Morning")
        fx(*args, **kwargs)         #arguments needs to be updated because of mfx
        print("Thanks for using this functions")
    return mfx

@greet              #1st way 
def hello():                
    print("Hello world")

@greet      #Decorator (modifies function)
def add(a,b):
    print(a+b)

hello()
greet(hello())       #2nd way
greet(add(4,6))       #2nd way


