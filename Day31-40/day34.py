#Day34 - Dictionary Methods in Python 


#Update:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
# old_dict.update(new_dict) 
info.update({'age':20})
info.update({'DOB':2001})
print(info)


#clear:
info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)

#printing an empty dictionary 
empt = {}
print(empt)
print(type(empt))


#pop
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)

#popitem: removes last key-value pair
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)


#del():
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)


info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)

#must see docs.python.org for more detailed 
#methods and information 

