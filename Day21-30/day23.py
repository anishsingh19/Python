#List Methods in Python
# append 
# sort 
# sort - reverse 
# reverse 
# index 
# count 
# copy 
# insert 
# extend 
# concatenating two lists 

l = [11, 45, 1, 2, 4, 6, 1]
print(l)

print("append")
l.append(7)
print(l)

print("sort")
l.sort()
print(l)

print("sort - reverse = True")
l.sort(reverse=True)
print(l)

print("reverse")
l.reverse()
print(l)

print("Index")
print(l.index(1))   #returns index of the first occurence
                    # of the list item

print("Count")   
print(l.count(1))         

print("Copy")
# m = l
# m[0] = 0
# print(l)

m = l.copy()
print(m)

print("Insert")
m.insert(1,899)
print(m)

print("Extend")
p = [998, 1000, 1100]
l.extend(p)   #open p and put it in 
print(l)      #the end of l

print("Concatenating 2 lists")
k = p + m
print(k)