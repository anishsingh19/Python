#Day22 Introduction to Lists in Python
# list
# print list 
# indexing 
# Negative Indexing 
# if item is present in the list
# Accessing elements of the list 
# List Comprehension

marks = [3,4,5, "mark", True]
print(marks)
print(type(marks))
print(len(marks))

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

print(marks[-3])        #Negative Indexing
print(marks[len(marks)-3])  #Positive Index
print(marks[5-3])
print(marks[2])

if 7 in marks:
    print("yes")
else:
    print("No")

print(marks)
print(marks[:])         #0:len[marks]
print(marks[1:-1])
print(marks[1:4])
print(marks[1:4:2])     #Jump index

#List Comprehension
lst = [i for i in range(4)]
print(lst)

lst = [i*i for i in range(10) if i%2==0]
print(lst)