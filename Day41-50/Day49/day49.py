#Day49 - File IO in Python 

# modes: 
# r,read(default)    
# w,write: deletes the existing data     
# a,append: adds data at the end 
# x,create
# t,text    (Eg:rt read as text)(default)
# b,binary for binary files like img,pdf etc


# #READING A FILE
f = open('myfile.txt','r')   #read cmd wont work
print(f)                     #if mode was w 
text = f.read()
print(text)
f.close()


#WRITING A FILE
# w creates a file which does not exists
f = open('myfile2.txt','w')  #mode a words as well 
f.write("Hello World")
f.close()


#Using with statement 
with open('myfile.txt','a') as f:
    f.write("This statement is added using with statement")
f.read()
f.close()














