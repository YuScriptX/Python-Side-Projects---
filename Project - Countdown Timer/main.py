# Countdown Timer

import time

my_time = int(input("Enter the time in sec: "))

for x in range(0, my_time):
    print(x)
    time.sleep(1)

print("Hi Guys!")