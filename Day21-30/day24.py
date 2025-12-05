#Day24 - Tuples
#immutable

tup1 = (1,5,6)
print(type(tup1), tup1)

tup2 = (1)       #single element must end with ,
print(type(tup2), tup2)

tup3 = (1,)
print(type(tup3), tup3)

print("Accessing items in Tuple")
tup4 = (1,2,76,342,32,"green", True)
print(type(tup4), tup4)
print(len(tup4))
print(tup4[0])
print(tup4[1])
print(tup4[2])
print(tup4[-2])
print(tup4[6])

if 342 in tup4:
    print("Yes 342 is present in this tuple.")

# Slicing in Tuples 
tup = tup4[1:4]
print(tup)

