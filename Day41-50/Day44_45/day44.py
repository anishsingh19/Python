#Day44 - How import works in Python 

#import pandas 
import math

print(math.floor(4.5775))
res = math.sqrt(9)
print(res)

from math import sqrt, pi  
# from math import *     # * to import all functions and 
res2 = sqrt(9) * pi      #variables from a module    
print(res2)

#as keyword 
from math import pi, sqrt as s
res2 = s(16) * pi      
print(res2)

import math as m
res2 = m.sqrt(25) * m.pi     
print(res2)


print(dir(math))                    #dir to view the names of all functions
print(math.nan, type(math.nan))     #and variables defined in a module.


#custom made module 
# from hey import welcome, boy
# from hey import*
# welcome()
# print(boy)

import hey as h 
h.welcome()
print(h.boy)


