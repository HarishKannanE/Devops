# Define Function

'''
def add(arg1, arg2):
    total = arg1 + arg2
    return total

out = add(1, 2)
print(out)
print(add(20, 30))
'''

'''
def adder(arg1, arg2):
    total = arg1 + arg2
    print(total)

adder(20, 30)
print(adder(30, 40))
'''
'''
def sum(arg):
    x = 0
    for i in arg:
        x = x + i
    return x

# out = sum([1, 2, 3])
# print(out)

sum([10, 20], [30, 40])
'''
# Default Argument

def greetings(msg="Morning"):
    print(f"Good {msg}")
    print("Welcome to the function.")

greetings()
greetings("evening")
