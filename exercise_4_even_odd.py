number = int(input("Enter Your number"))
#for number in range(1, 50):
if (number % 2) == 0:
    print(f"The {number} is even")
elif (number % 2) != 0:
    print(f"The {number} is odd")
else:
    print(f"{number} is invalid")
