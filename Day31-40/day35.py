#Day35 - For Loop with else in Python 
# if else statement gets executed, it represents
# loop has ended successfully 


for i in range(5): #try [] in place of range(5)
    print(i)
else:
    print("Sorry no i")


#Guess for the following codes if else statement
#will be executed or not
print("Problem Set 1")
for i in range(6): 
    print(i)
    if i == 4:
        break
#(statements in the else block will be 
# executed after all iterations are complete)
else:
    print("Sorry no i")


print("Problem Set 2")
i = 0
while i<7:
    print(i)
    i = i + 1
    if i == 4:
        break

else:
    print("Sorry no i")


print("Problem Set 3")  
i = 0
while i<7:
    print(i)
    i = i + 1
    # if i == 4:
    #     break

else:
    print("Sorry no i")


print("Problem Set 4")  
for x in range(5):
    print("iteration on {} in for loop".format(x+1))
else:
    print("else block in loop")
print("Out of Loop")