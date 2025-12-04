#Day12 Strings Slicing & Operations on Strings

# Access first five elements of the string 
names = "Harry,John"
print(names[0:5]) 
print(names[5])       #printing comma 
print(len(names))

#Slicing 
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")
print(fruit[0:4])
print(fruit[:4])
print(fruit[1:4])
print(fruit[1:])

#negative indexing 
print(fruit[0:-3])          #print(fruit[0:len(fruit)-3])
print(fruit[-3:-1])   #2:4


#Quick Quiz
nm = "Harry"
print(nm[-4:-2])        #estimated output ar
