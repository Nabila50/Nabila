# 17. Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output: 9 days


first = input('enter your 1st date: ')
second = input('enter your 2nd date: ')

first = first.split(',')
second= second.split(',')

first_day = (int(first[0])*365 + int(first[1])*30 + int(first[2]))
second_day = (int(second[0])*365 + int(second[1])*30 + int(second[2]))

day = first_day - second_day
print(f"the result will be {day} days")


# first_date = input("enter your 1st date: ")
# second_date = input("enter your 2nd date: ")
#
# first_date = first_date.split(',')
# second_date = second_date.split(',')
#
# day_of_first_date = (int(first_date[0])*365 + int(first_date[1])*30 + int(first_date[2]))
# day_of_second_date = (int(second_date[0])*365 + int(second_date[1])*30 + int(second_date[2]))
#
# day = day_of_first_date - day_of_second_date
#
# print(f"the difference from first day to second day: {day} days")
