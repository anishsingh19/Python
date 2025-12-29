#Day51 - seek()_tell() and other functions


#seek() and tell() functions
with open('file.txt', 'r') as f:
    print(type(f))
    # Move to the 10th byte in the file 
    f.seek(10)

    # Read the next 5 bytes
    print(f.tell())
    data = f.read(5)
    print(data)


# truncate() function 
with open('sample.txt', 'w') as f:
    f.write("Hello World!")
    f.truncate(5)   #defines number of bytes 
                    #you would like to have 
                    #for the file.

with open('sample.txt', 'r') as f:
    print(f.read())



























