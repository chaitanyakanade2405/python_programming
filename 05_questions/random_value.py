import random

members = ["Chaitanya", "Sachin", "Virat", "Rohit", "Dhoni"]
leader = random.choice(members)
print(leader)

for i in range(3):
    print(random.randint(10,20))