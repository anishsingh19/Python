#Day41 - Short hand if else Statements
#If-Else in One Line 


a = 330 
b = 3303 
print("A") if a > b else print("=") if a == b else print("B")       #1

print(9) if a>b else ""         #2

c = 9 if a>b else 0             #3
print(c)                                                                                                   


#result = value_if_true if condition else value_if_false
#Above syntax is equivalent to the following 
# if condition:
#     result = value_if_true
# else:
#     result =  value_if_false


