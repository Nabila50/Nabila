#2. Write a program to print the sum of two numbers.

a = int(input('Write a number'))
b = int(input('Write an another number'))
sum= 0
for x in (a, b):
      sum = sum + x

print(sum)


# another way
number1 = int(input('give 1st number\n'))
number2 = int(input('give 2nd number\n'))

summation = number1 + number2

print(f'summation of {number1} and {number2} is {summation}')
