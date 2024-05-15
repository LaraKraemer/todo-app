import random

# input user
user_lower = int(input("Enter a lower bound: "))
user_upper = int(input("Enter a upper bound: "))

# random number generator
randNo = random.randrange(user_lower, user_upper + 1)
print("The number generated is: ", randNo)