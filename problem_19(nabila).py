#Write a Python program to compute the future value of a specified principal amount, rate of interest, and the number of years.
#Test Data : amt = 10000, int = 3.5, years = 7
#Expected Output: 12722.79

amount = float(input('enter your amount'))
interest = float(input('enter the amount of intereset'))
years = int(input('how many years?'))

value = amount * (1+interest/100) ** years
print(f"future value will be {value}")