#Day58 - Constructors in Python 
# def__init__(self):

# a. special method in a class used to create and initialize an object of a class
# b. invoked automatically when an object of a class is created 
# c. main purpose is to initalize or assign values to the data members of that class
# d. it cannot return any value other than None

# Type1 - Parameterized Constructor   def __init__(self, name, age):
# Type2 -     Default Constructor     def __init__(self):


class Person:
    name = "Harry"
    occ = "Developer"

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person()
print(a.name)

a.name = "Divya"        #Constructor is used to overcome this
a.occ = "HR"            #problem 
a.info()



print("Using Constructor:")
class Person:
    
    def __init__(self, n, o):
        print("Hey I am a Person")
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")

a = Person("Harry", "Developer")
b = Person("Divya", "HR")

a.info()     #Comment these and run 
b.info()

# c = Person()   #Try running this to understand self argument 
# c = Person(1,2,3)   #Try running this to understand self argument 
#c is passed as self and hence only 2 arguments are required to give 

