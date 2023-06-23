planet1 = "Closest of Sun."

# Slicing
print(planet1)
print(planet1[0])
print(planet1[1])
print(planet1[2])

# Negative slicing
print(planet1[-1])
print(planet1[-2])
print(planet1[-3])

# Slicing a striing, get a substring from a string
print(planet1[1:4])
print(planet1[:])
print(planet1[0:7])

# Slicing tuple
devops = ("Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible")

print(devops[0])
print(devops[4])
print(devops[-1])
print(devops[2:5])
print(devops[2:5][0])
print(devops[2:5][0][5:11])

# Slicing sets
devops = ["Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible"]

print(devops[0])
print(devops[4])
print(devops[-1])
print(devops[2:5])
print(devops[2:5][0])
print(devops[2:5][0][5:11])


# Dictionary  Example
skills = {"DevOps":("Jenkins", "Python", "Ansible"), "Development":["Java", "NodeJS", ".net"]}

print(skills)
print(skills["DevOps"])
print(skills["Development"])
print(skills["DevOps"][2])
print(skills["DevOps"][2][:4])