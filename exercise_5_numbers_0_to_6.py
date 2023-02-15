#Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
#Note : Use 'continue' statement.
a = 3
b = 6

for i in range (0, 6+1):
    if i == a or i== b:
        continue
    else:
        print(f"The numbers are {i}")