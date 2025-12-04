#Day14 If Else Conditional Statements 

a = int(input("Enter your age: "))
print("Your age is:", a)

# Conditional operators
# >, <, >=, <=, ==, !=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)

#01
if(a>=18):
    print("You can vote.")          #Indentation here
else:
    print("You cannot vote")
    print("No")         #this is in else statement 
print("Yayy")       #this is out of else statement 

#02 IF ELSE Statement 
applePrice = 210
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")

#03 IF ELIF Statement 
applePrice = 10
budget = 200
if (budget - applePrice > 50):
    print("Alexa, add 1 kg Apples to the cart.")
elif(budget - applePrice > 70):
    print("It's okay you can buy.")
else:
    print("Alexa, do not add Apples to the cart.")


num = int(input("Enter the value of num: "))
if (num < 0):
    print("Number is Negative.")
elif (num == 0):
    print("Number is Zero.")
elif (num == 999):
    print("Number is Special.")
else:
    print("Number is Positive.")


#04 Nested if Statements
num = int(input("Enter a Number: "))
if (num < 0):
    print("Number is Negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is Zero.")



