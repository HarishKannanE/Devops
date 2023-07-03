# Nested For Loop
'''
VACCINES = ("Moderna", "Pfizer", "Sputnik V", "Covaxin", "AstraZeneca")

for vac in VACCINES:
    print("")
    print("I would like to take a shot of ")
    print("")
    for i in vac:
        print(i)
'''

# Nested While Loop

import time

x = 2

while True:
    print("Value of x is", x)
    print("Looping")
    x *= 2
    time.sleep(1)