#Day18 While Loops

for i in range(3):
    print(i)

i = 0
while(i < 3):
    print(i) 
    i = i + 1
    

i = int(input("Enter the number: "))       #This is an
while(i<=38):                              #example 
    i = int(input("Enter new value: "))    #of Do-While
    print(i)                               #in Python

print("Done with the Loop")


#Decrementing Loop
count = 5
while (count > 0):
    print(count)
    count = count - 1 


#Else with While Loop
count = 5
while (count > 0):                  #As soon as this 
    print(count)                    #While loop ends
    count = count - 1               #else statement is
else:                               #executed
    print("I an inside else")


#Do-While loop in Python  

#example of do-while in other language; C++
# do {
#     loop body;
# }while(condition);
