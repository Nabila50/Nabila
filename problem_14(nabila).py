# 14. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

name = str(input('Please enter your First and Last Name together:'))
a = name[::-1]
print(f"the reverse name is {a}")

#----------------------------------------------------------------------------------------------
# for i in name[::-1]:
#     if i == name:
#         print(f" the name is not reverse {i}")
#     elif i != name[::-1]:
#         print(f"the name is reversed {i}")
    # else:
    #     print('the name is not the given name')
#-------------------------------------------------------------------------------------------
for i in reversed(name):
    print(i)
