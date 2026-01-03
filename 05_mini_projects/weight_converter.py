weight = int(input("Weight: "))
unit = input("(L)bs or (K)gs: ")

if unit.upper()=="L":
    converted_weight=weight * 0.45
    print(f"Weight is: {converted_weight} kilos")

else:
    converted_weight=weight / 0.45
    print(f"Weight is: {converted_weight} pounds")