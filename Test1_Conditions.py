print("This IT Organization has various skill sets.")
print("Find out your match.")

print("Enter Capitalised values: ")

Devops = ["Jenkins", "Ansible", "Bash", "Python", "Puppet", "Dockers", "Kubernetes", "Terraform"]
Development = ("Nodejs", "Angularjs", "Java", ".net", "Python")
emp1 = {"Name":"Santa", "Skill":"Blockchain", "Code":1024}
emp2 = {"Name":"Rocky", "Skill":"AI", "Code":1218}

usr_skill = input("Enter a desired skill: ")
# print(usr_skill)

# Check in the database if we have this skill 

if (usr_skill in Devops):
    print(f"We have {usr_skill} in DevOps Team.")
elif(usr_skill in Development):
    print(f"We haev {usr_skill} in Development Team.")
elif(usr_skill in emp1.values()) or (usr_skill in emp2.values()):
    print("We have contract employees with this skill.")
else:
    print("Skill not found.")
    print("Please check if you have entered value in capitalize or check teh spelling.")
    