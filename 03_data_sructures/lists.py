# name = ["Chaitanya","Sachin","Rohit","Virat","Dhoni"]
# print(name[1:3])

numbers = [2,3,5,69,2,4,72,9,4]
max = 0
# numbers.sort()
# print(f"Largest Number: {numbers[-1]}")

for number in numbers:
    if number > max:
        max = number
print(max)