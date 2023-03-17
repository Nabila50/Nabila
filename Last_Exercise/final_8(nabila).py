# 8.	Write a program to find the sum of digits of a given number.

num = input('give a number: ')

sum = 0

for i in num:
    sum += int(i)

print(sum)
