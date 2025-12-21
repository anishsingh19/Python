#Day36 - Exception Handling in Python


a = input("Enter the number:")
print(f"Multiplication table of {a} is:")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except: #(Exception as e:) This is optional
    print("Invalid Input!")

print("Some imp lines of code")
print("End of program")


#Multiple except blocks are allowed
try:
    num = int(input("Enter an integer:"))
    a = [6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index Error")
