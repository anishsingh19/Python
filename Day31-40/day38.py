#Day38 - Raising custom errors in Python

a = int(input("Enter any value between 5 and 9:"))
if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")


#Quick Quiz: copy the above code and edit it such 
# a way that "quit" as input should not raise an error 
a = int(input("Enter any value between 5 and 9:"))
if(a==str(quit)):
    print("ok")
elif(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")

