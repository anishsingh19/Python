#Day32 - Set Methods in Python

#1-Union
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print("union:", s1.union(s2))

print(s1,s2)

#2-Update
s1.update(s2)
print("s1 updated:", s1, s2)

s1 = {1, 2, 5, 6}
#3-Intersection 
s3 = s1.intersection(s2)
print("Intesection:", s3)

s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
#4-Intersection Update
print("Intersection Update:", s1.intersection_update(s2))
print(s1)

s1 = {1, 2, 5, 6}
s2 = {3, 6, 7, 2}
#5-Symmetric_difference
sym = s1.symmetric_difference(s2)
print(sym)

#6-Symmetric_difference_update
#this updates into the existing set from another set 
print("symmetric_difference_update", s1.symmetric_difference_update(s2))

# 7-Difference 
# prints only the items that are only present in the 
# original set and not in both the sets
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)

#8-Difference_update 
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
print(cities.difference(cities2))

#9-isdisjoint
#checks if items of given set are present in another set
#returns false if items are present
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print("isdisjoint:", cities.isdisjoint(cities2))

#10-issuperset
# checks if all the items of a particular set are present in the original set
# returns True if all the items are present, else it returns False
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print("issuperset:", cities.issuperset(cities2))
cities3 = {"Tokyo", "Madrid"}
print("issuperset:", cities.issuperset(cities3))

#11-issubset
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print("issubset:", cities2.issubset(cities))


#12-add
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

#13-update
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print("cities updated:", cities)

#14-remove
#raises an error if item is not present in the set
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print("Removing Tokyo:",cities)

#15-Discard
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.discard("Dubai")
print("Discarding Dubai:",cities)

#16-pop
#removes the last item of the set but we don't know
#which item will get removed as sets are unordered
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print("Poped item is", item)

#17-del
# NOT a Method, rather it is a keyword which
# deletes the entire set
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
# print(cities)

#18-clear
# clears all items in the set and prints an empty set 
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

#Check if item exists
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")

