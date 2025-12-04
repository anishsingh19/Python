# Day20 Functions in Python

def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def greatnum(a,b):
    if a > b:
        print("num", a, "is bigger than num", b)
    else:
        print("num", b, "is bigger than num", a)

def islesser(a,b):
    pass
    # if ( a < b):
    #     print("First number is lesser")
    # else:
    #     print("Second number is lesser")

a = 9
b = 8
gmean1 = (a*b)/(a+b)
print(gmean1)
calculateGmean(a,b)
greatnum(a,b)

c = 8
d = 7
gmean2 = (c*d)/(c+d)
print(gmean2)
calculateGmean(c,d)
#islesser(c,d)

# def greatnum(a,b):
#     if a > b:
#         print("num", a, "is bigger than num", b)
#     else:
#         print("num", b, "is bigger than num", a)
