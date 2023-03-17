# 9. Write a program to check whether a given number is even or odd
number = int(input('write a number\n'))

for i in [number]:
    if i % 2 == 0:
        print(f"The given {i} is even number")
        #if i == number:

    else:
        print(f"The given {i} is an odd number")
