#Day57 - Classes and Objects in Python 
# A class is a blueprint or a template for creating objects,
# providing initial values for state (member variables or attributes),
# and implementations of behavior (member functions or methods). The 
# user-defined objects are created using the class keyword. 


class Person:
    name = "Henry"      #Three properties
    occupation = "ML Engineer"
    networth = 10

    def info(self):      #one Methods 
        print(f"{self.name} is a {self.occupation}")


a = Person()            #Creating an Object
b = Person()
c = Person()


a.name = "A_John"           #Changing properties of class Person 
a.occupation = "Quantitative Analyst"
print(a.name, a.occupation)
a.info()


b.name = "B_Arjun"
b.occupation = "Data Scientist"
b.info()


c.info()

#self parameter: a reference to the current instance of the class, 
# and is used to access variables that belongs to the class.
# (self means woh object jis par yeh method call ho raha hai)


    