numbers = [1,5,6,7,7,5,4,3,6]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)