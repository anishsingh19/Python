#Day33 - Dictionaries in Python 
# fact: Dictionaries are ordered from Python 
# v 3.7 onwards, before it were unordered

dic = {
    "Harry": "Human being",
    "Spoon": "Object",
    344: "Harry",
    56: "Shubham",
    678: "Zakir",
    567: "Neha"
}
print(dic["Harry"])
print(dic[567])


info = {'name':'Karan', 'age':19, 'eligible':True}
print(info) 

#Accessing single values:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name']) #throws an error if value is not present in the dictionary 
print(info.get('name'))


#Accessing multiple values:
print(info.keys())
print(info.values())

for key in info.keys():
    print(info[key])

for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")


#Accessing key-value pairs:
print(info.items())

for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")

