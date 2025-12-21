#Day37 - Finally Keyword in Python
#code in finally clause will be executed in any situation 


try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index:"))
    print(l[i])
except:
    print("Some error occurred")

# finally:
#     print("I am always executed")
print("I am always executed")


#finally keyword is most useful in function
def func1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index:"))
        print(l[i])
        return 20
    except:
        print("Some error occurred")
        return 0

    finally:
         print("I am always executed")
    print("I am always executed")  #Here, this will 
    #not be executed ever 

x = func1()
print(x)

