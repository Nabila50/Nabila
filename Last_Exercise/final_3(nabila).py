# 3. Write a program to print the product of two numbers.

a = int(input('write a number'))
b = int(input('write an another number'))

multiple = 1

for i in (a, b):
    multiple = multiple * i

print(multiple)

# another way is----------------------

multiple = a * b
print(multiple)