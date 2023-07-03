# Variable Length Arguments *args (Non Keyword Arguments)

'''
def order_food(min_order, *args):
    print(f"You have ordered : {min_order}")
    for item in args:
        print(f"You have ordered : {item}")
    print("Your food will be delivered in 30 mins.")
    print("Enjoy your order.")

order_food("Salad", "Biriyani", "Chicken Curry")
'''

# Variable Length Arguments **kwargs (keyword Arguments)

import random

def time_activity(*args, **kwargs):
#    print(args)
#    print(kwargs)
    min=sum(args) + random.randint(0, 60)
#    print(min)
    choice=random.choice(list(kwargs.keys()))
    print(choice)
    print(f"You have to spend {min} mins for {kwargs[choice]}")

time_activity(10, 20, 30, hobby="Dance", sport="Boxing", fun="Driving", work="DevOps")