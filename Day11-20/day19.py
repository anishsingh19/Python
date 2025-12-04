#Day19 Break and Continue

#Break Statement 
for i in range(12):
    if (i == 10):
        print("Break the Loop")
        break              #loop ko chodkar nikal gaya
    print("5 X", i+1, "=", 5*(i+1))

# for i in range(12):
#     print("5 X", i+1, "=", 5*(i+1))
#     if (i == 10):
#         break    

print("********Continue Statement********")
#Continue Statement 
for i in range(12):
    if(i == 10):
        print("Skip the iteration")
        continue
    print("5 X", i+1, "=", 5 * (i+1))


#Emulating Do-While Loop or Exit-Controlled Loop 
# in Python using 'infinite while loop' with a 'break 
#statement' wrapped in an 'if statement' that checks a 
# given condition and breaks the iteration if that 
# condition becomes  true 

i = 0
while True:     #infinite while loop
    print(i)
    i = i + 1
    if(i%100 == 0):    #runs till i = 100
        break

while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number > 0:         #contunues to run if 
        break                  #entered number is a 
                               #positive number