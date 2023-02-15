#5.  Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note: Use the 'continue' statement.
# Expected Output : 0 1 2 4 5
a = 3
b = 6
c = 5

for i in range(0, 6+1):
    if i == a or i == b:
        continue
    else:
        print(f"The numbers are {i}")