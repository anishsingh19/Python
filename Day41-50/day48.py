#Day48 - Local vs Global Variables in Python 

x = 123         #Global Variable 
print(x)
z = 45
print(z)

def hello():
    x = 57      #Local Variable
    y = 78
    global z
    z = 89
    print(f"{y}")
    print(f"The local x is {x}")
    print("Hello User")


hello()
print(f"The Global x is {x}")
print(f"The Global z is {z}")   
   










