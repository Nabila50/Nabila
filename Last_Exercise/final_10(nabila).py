# 10. Write a program to check whether a given number is a prime number or not

num = int(input('write a number'))


for i in [num]:
    if i % 2 == 0:
        print(f"{num} is not a prime number")
        break
    elif i % 2 != 0:
       print(f"{num} is not a prime number")
    else:
        print(f"{num} is a prime number")

