
number = int(input("your number: "))
number_to_make = int(input("Number to make: "))


if 0 > number or number > number_to_make:
    print("You can't select that number")
else:
    complement = -number + number_to_make
print(f"The number to add to make {number_to_make} is {complement}")






