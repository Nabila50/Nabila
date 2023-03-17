# 6. Write a program to find the factorial of a given number.

number = int(input('write a number\n'))

factorial = 1

for i in range(1, number):
     factorial = factorial * i
     print(factorial)


# another way to direct find factorial number:

if number >=0:
    if number == 0 and number == 1:
        pass

    else:
        for i in range(2, number):
            number *= i

        print(number)
