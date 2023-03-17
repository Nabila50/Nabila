# age 1-15: you're not eligible for the community
# age >15 <40 : you're eligible
# else : tumi ghure berao


# age = 1
# for i in range(20, 30 + 1):
#     if i >= age:
#         print(f"your age is {i}, You are not our neighbour. So you are not allowed in our community")
#         continue
#
#     elif i <= age:
#         print(f"Sorry, your age is only {i}, you cannot go to the inside")
#         break
#
#     else:
#         print(f" Congratulations, Your age is {i}, Welcome to our new Home")

for age in range(20, 51):
    if 25 < age < 40:
        print(f"you're eligible to enter into the community [Age:{age}]")
    else:
        continue