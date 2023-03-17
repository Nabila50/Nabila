# 5. Write a program to find the second largest among three numbers.

num1 = int(input('give 1st number: '))
num2 = int(input('give 2nd number: '))
num3 = int(input('give 3rd number: '))

if num1 > num2 and num1 >num3:
    if num2 > num3:
        print(num2)
    else:
        print(num3)

elif num2 > num1 and num2 >  num3:
    if num1 > num3:
        print(num1)
    else:
        print(num3)

else:
    if num1 > num2:
        print(num1)
    else:
        print(num2)