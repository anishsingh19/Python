#Day30 - Recursion in Python

# factorial(n) = n * factorial(n-1)
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))
print(factorial(4))
print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1  

#Quick Quiz: Write a program to print the
# Fibonacci Sequence
# f(0) = 0 
# f(1) = 1 
# f(2) = f(1) + f(0) 
# f(n) = f(n-1) + f(n-2)
# 0 1 1 2 3 5 8 13 ...


def Fibonacci(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

n = int(input("Enter the number for which you want Fibonacci Sequence:"))
print(Fibonacci(n))

