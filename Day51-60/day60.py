#Day60 - Getters and Setters in Python 
# - Getters in Python are methods that are used to access the values 
# of an object's properties. (Creating new method which behaves like a property)
# - They are used to return the value of a specific property, and are 
# typically defined using the @property decorator. 

#Setter 
# - note that the getters do not take any parameters and we cannot set the 
# value through getter method. 
# - For that we need setter method which can be added by decorating method with 
# @property_name.setter
# This can be useful for encapsulation and data validation


#Example of a simple class with a getter method
class MyClass:
  def __init__(self, value):
      self._value = value
    
  def show(self):           #method
    print(f"Value is {self._value}")
  

  @property                     #Getter method
  def ten_value(self):          #ten_value is actually a method but because of 
                                    #decorator it looks like a property 
     return 10 * self._value    #returns 10 times the value of self
 

#   @ten_value.setter           #Setter 
#   def ten_value(self, new_value):         #sets _value because ten_value also derives its value 
#       self._value = new_value/10           #from _value 



obj = MyClass(10)           #object
print(obj._value) 

obj.show()                  #show method is called 


# obj.ten_value = 67        #This will throw an error if setter is commented out 
print(obj.ten_value)            # /disabled in the above code 










































