# number = int(input("Enter Your number"))
# #for number in range(1, 50):
# if (number % 2) == 0:
#     print(f"The {number} is even")
# elif (number % 2) != 0:
#     print(f"The {number} is odd")
# else:
#     print(f"{number} is invalid")

odd = 0
even = 0

for i in range(1, 46):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"odd numbers:{odd}, even numbers:{even}")
