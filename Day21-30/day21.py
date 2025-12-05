# Day21 Function Arguments in Python
#1-Default Arguments
#2-Keyword arguments
#3-Required Arguments
#4-Variable-length arguments
#return statement

def average(a=3,b=3):       #1-Default Arguments
    print("The average is ", (a+b)/2)

# average()             #1-Default Arguments
# average(4,6)
average(b=8, a=6)       #2-Keyword arguments 
                        #Order doesn't matter


def average(a,b=3):      #3-a is Required Arguments
    print("The average is ", (a+b)/2)

average(a=5)

# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)
# name("Peter", "Quill")

#4-Variable-length arguments
def avg(*numbers):             #* for tuple
    print(type(numbers))       #** for dictionary
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is:", sum/len(numbers))
    
avg(4,5,4)


#4-Variable-length arguments
#with return statement
def avg(*numbers):             #* for tuple
    print(type(numbers))       #** for dictionary
    sum = 0
    for i in numbers:
        sum = sum + i
    #print("Average is:", sum/len(numbers))
    #return 7
    return sum/len(numbers)

c=avg(4,5,4)
print(c)