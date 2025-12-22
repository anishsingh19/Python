#Day50 - read()_readlines() and other methods 

#readline()
f = open('fifty.txt','r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)


#Use Case in Data Science 
f = open('marks.txt','r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])

    print(f"Marks of Student {i} in Maths is: {m1}")
    print(f"Marks of Student {i} in English is: {m2}")
    print(f"Marks of Student {i} in Science is: {m3}")

    print(line)


# writelines()      does not add newline characters 
                  # between the strings in the sequence
f = open('myfile2.txt','w')
lines = ['line 1\n', 'ine 2\n', 'line 3\n']
f.writelines(lines)
f.close()












