# String Build in Methods/Functions
'''
message = "how are you"
print(message) 
print(message.capitalize())
Message = message.capitalize()
print(Message)
'''
# dir() function
'''
print(dir(""))
print(dir([]))
print(dir({}))
print(dir(()))
'''
'''
message = "how are you"

print(message.upper())
print(message.islower())
print(message.isupper())

print(message.find("how"))
'''
'''
message = "how are you"

seq1 = ("192", "168", "1", "1")
print(".".join(seq1))
print("/".join(seq1))
'''
'''
mountains = ["Everest", "Himalayan", "Sahyadri", "Alps", "K2", "Mt Hood"]
print(mountains)

mountains.append("Oregon Mount")
print(mountains)

mountains.extend(["Satpuda", "Mt Rainer"])
print(mountains)

mountains.insert(2,"Mt Abu")
print(mountains)

mountains.pop()
mountains.pop()
print(mountains)

mountains.pop(2)
print(mountains)
'''


skills = {"DevOps":("Jenkins", "Python", "Ansible"), "Development":["Java", "NodeJS", ".net"]}

print(skills.keys())
print(skills.values())
skills.clear()
print(skills)
