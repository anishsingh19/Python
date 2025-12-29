#Day52 - Lambda functions in Python 
# small anonymous funtion without a name
# lambda arg: expression
# can include multiple statements, but limited to single expression 
def double(x):
    return x*2
print(double(10))

doub = lambda x: x*2
print(doub(4))

cube = lambda x: x*x*x 
print(cube(5))

avg = lambda a,b: (a+b)/2
print(avg(8,6))


# Passing function as arguments
def appl(fx, value):
    return 6 + fx(value)

print(appl(cube,2))   #8+6
print(appl(lambda x: x*x*x,2))   #8+6


x = input("Enter 1st number to multiply: ")
y = input("Enter 2nd number to multiply: ")
lambda x,y: print(f'{x} *{y} = {x * y}')


















