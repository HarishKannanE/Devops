# Arithemetic Operators
'''
x = 3
y = 5

total = x + y
print(total)

total = x - y
print(total)

total = x * y
print(total)

total = x / y 
print(total)

total = x % y
print(total)

total = y**x
print(total)
'''
# Comparison Operators
'''
a = 30
b = 60

out = (a < b)
print(out)

out = (a > b)
print(out)

out = (a == b)
print(out)

out = (a != b)
print(out)

out = (a >= b)
print(out)

out = (a <= b)
print(out)
'''

# Assignment Operators
'''
c = 0
d = 1

c+=d # c = c + d
print(c)

c-=d # c = c - d
print(c)
'''
'''
# Logical Operators

#and
#or
#not

a = 40
b = 60

x = 2
y = 3

out = (a < b) or (x > y)
print(out)

out = (a > b) or (x < y)
print(out)

out = (a < b) and (x < y)
print(out)

out = (a > b) and (x > y)
print(out)

out = not(a > b)
print(out)
'''

# Membership Operators
'''
first_tuple = ("str1", "Devops", 47, "num1", 1.5)
ans = "Devops" in first_tuple
print(ans)

first_tuple = ("str1", "Devops", 47, "num1", 1.5)
ans = "Devops" not in first_tuple
print(ans)
'''

# Identity Operators

a = 12 
b = 15

result = a is b
print(result)

result = a is not b
print(result)