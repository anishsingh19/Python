#Day54 - is vs == in Python 
# is operator compares the identity of 2 objects
# == operator compares the values of the objects

a = 4
b = "4"
print(a is b)   #compares exact location of object in memory
print(a == b)   #compares value

print("Comparing list")
l = [1,2,45]
l2 = [1,2,45]
print(l is l2)
print(l == l2)

print("Comparing Constant/immutable")
c = 5
d = 5
print(c is d)
print(c == d)

c = "harry"
d = "harry"
print(c is d)
print(c == d)

c = (1,2,5)
d = (1,2,5)
print(c is d)
print(c == d)

c = None
d = None
print(c is d)
print( c is None)
print(c == d)





































