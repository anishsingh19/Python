# Strings in Python

name = 'Harry'
friend = "Rohan"

print("Hello, " + name)

#print -> He said, "I want to eat an apple." 
                                             #hint: using escape sequence
apple = "He said, \"I want to eat an apple.\""   
apple2 = 'He said, "I want to eat an apple."'   
apple3 = "He said, 'I want to eat an apple.'"   

print(apple)
print(apple2)
                        #Multiline string 
chat = ''' hello 
hi 
how are you doing? 
i'm good, thank you. 
'''
print(chat)

#String is like an array; a collection of items 
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5])        #Throws an Error

'''accessing Characters of a String
for loop 
for character in name:
    print(character)
'''

print("Lets use a for loop\n")
for character in apple:
    print(character)

