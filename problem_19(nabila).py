#Write a Python program to compute the future value of a specified principal amount, rate of interest, and the number of years.
#Test Data : amt = 10000, int = 3.5, years = 7
#Expected Output: 12722.79

amt = [10000]
interest = [3.5]
years = 7

for i in amt:
    if i >= 10000*3.5:
        print(f"the total amount with interest is {i}")