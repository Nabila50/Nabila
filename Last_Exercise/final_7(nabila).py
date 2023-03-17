# 7.	Write a program to find the sum of first n natural numbers.
n_number = int(input('enter the number: '))

sum = 0

for i in range(0, n_number+1):
    sum += i
print(sum)
