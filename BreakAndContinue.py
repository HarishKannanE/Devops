# Break Statement 
'''
for i in "Devops":
    print(i)
    if i == "o":
        print("Found my data.")
        break
print("Out of loop.")
'''

# Continue Statement 
'''
for i in "Devops":
    if i == "o":
        print("Found my data.")
        continue
    print(f"Value of i is {i}")
print("Out of loop.")
'''
'''
import random

VACCINES = ["Moderna", "Pfizer", "Sputnik V", "Covaxin", "AstraZeneca"]

random.shuffle(VACCINES)
print(VACCINES)

Lucky = random.choice(VACCINES)
print(Lucky)

for vac in VACCINES:
    print(f"*** Testing Vaccine {vac} ***")
    if vac == Lucky:
        print("##################################")
        print(f"{Lucky} Vaccine, Test Successfull")
        print("##################################")
        break
    print("#####################")
    print("*** Test Failed ***")
    print("#####################")
    print("")
'''

import random

VACCINES = ["Moderna", "Pfizer", "Sputnik V", "Covaxin", "AstraZeneca"]

Lucky = random.choice(VACCINES)

for vac in VACCINES:
    print(f"*** Testing Vaccine {vac} ***")
    if vac == Lucky:
        print("##################################")
        print(f"{Lucky} Vaccine, Test Successfull")
        print("##################################")
        print("")
        continue
    print("#####################")
    print("*** Test Failed ***")
    print("#####################")
    print("")