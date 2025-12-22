#Day42 - Enumerate Funtion in Python


marks = [12, 56, 32, 98, 12, 42, 1, 4]

index = 0
for mark in marks:
    print(mark)  
    if(index == 3):
        print("Henry, Awesome!")
    index+=1

print("Doing the same using Enumerate Function")
for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("Henry, Awesome!")


#Loop over a list and print the index (starting at 1) 
# and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


for index, mark in enumerate(marks, start=1):
    print(mark)
    if(index == 3):
        print("Henry, Awesome!")


s = 'hello'
for index, c in enumerate(s):
    print(index, c)

