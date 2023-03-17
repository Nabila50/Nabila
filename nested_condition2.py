age = int(input('Enter your age:\n'))

if 18 <= age <= 25:
    print("he is matured but not adult")
elif 25 < age <= 35:
    print("he is adult but not old")
elif age > 35:
    print("he is old")
else:
    print("get the kid kicked out")
