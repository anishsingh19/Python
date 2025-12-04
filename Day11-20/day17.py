#Day17 For Loops

name = "Abhishek"
for i in name:
    print(i)
    
name = "Abhishek"
for i in name:
    print(i, end=", ")


#List
colors = ["\nRed", "Green", "Blue", "Yellow"]
for color in colors:
    print(color);
    for i in color:
        print(i)



print("Range Function")
for k in range(5):
    print(k + 1)

print("#2")
for k in range(1,9):
    print(k)


print("Quick Quiz:") #Explore Step funtion in Range
for i in range(0,26,5):
    print(i)
