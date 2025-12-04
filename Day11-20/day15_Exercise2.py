#Day15 Exercise2 - Good Morning Sir

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hr = int(time.strftime('%H'))
print(hr)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime

if (hr < 12):
    print("Good Morning Sir");
elif (hr > 12) and (hr < 16):
    print("Good Afternoon Sir");
else:
    print("Good Evening Sir");
