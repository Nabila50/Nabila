# # Write a Python program to convert the distance (in feet) to inches, yards, and miles.

# feet to inches conversion
# 1 feet = 12 inches
feet = float(input('enter your feet\n'))
inches = feet*12
print(f"{feet} feet is equal to {inches:.2f} inches")

# conversion from feet to yards
#1 yard = 3 feets
yards = 1/3
print(f"{feet} feet is equal to {yards:.3f} yards")

# conversion from feet to miles
# 1 mile = 5280 feet
miles = 1/5280
print(f"{feet} feet is equal to {miles:.9f} miles")
