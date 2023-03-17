age = int(input("Enter your age:\n"))

if 0 <= age <= 12:
    print("Kid is free in our metro-rail service")
elif 12 < age <= 50:
    print("He/She have to buy regular ticket")
elif 50 < age <= 80:
    print("He/She can buy metro-rail old citizen facilities ticket")
elif 80 < age <= 100:
    print("Old citizen is free in metro-rail service ")
else:
    print("He/She is not allowed in our metro-rail service. Thank you!")
