#Day26 - Exercise#2 Solution (day15)

import time
t = time.strftime('%H:%M:%S')
print(t)
hr = int(time.strftime('%H'))
# hr = int(input("Enter hour:"))
print(hr)

# https://docs.python.org/3/library/time.html#time.strftime

if (hr>=0 and hr<12):
    print("Good Morning Sir");
elif (hr >= 12) and (hr < 16):
    print("Good Afternoon Sir");
else:
    print("Good Evening Sir");
