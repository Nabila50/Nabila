# 11. Write a program to generate a Fibonacci sequence of n numbers.
n = int(input('give a number: '))
a= 0
b= 1

while n > b:
    print(b)
    a, b = b, a + b