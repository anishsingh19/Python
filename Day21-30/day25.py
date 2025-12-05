# Day25 - Operations on Tuples in Python


# Manipulating Tuples 
countries = ("Spain", "Italy", "India", "England", "Germany")
print(countries)

#convert to list to make changes in tuple
temp = list(countries)
temp.append("Russia")       #add item
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item

countries = tuple(temp)
print(countries)


# Merging Tuples 
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

#Occurrences of an element in Tuple
tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple1.count(3)
print('Count of 3 in tuple1 is:', res)

#First occurrence of an element 
tuple = (0, 1, 2, 31, 2, 3, 1, 3, 2, 3, 5, 6,)
res = tuple.index(3)
res2 = tuple.index(3, 6, 8)
print('First occurrence of 3 is', res)
print(res2)



