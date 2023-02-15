#7. Check if a given number is an Armstrong number or not.
number = input()

areas = 1
for i in number:
    areas += int(1)**len(number)
    print(areas)