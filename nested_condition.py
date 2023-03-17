age = int(input("Enter your age: "))
gender = input("What's your Gender? :")

# eligibility: for boys >10 years, for girls > 12 years

if gender == 'male':
    if age == 10:
        print("you're 1 year away from flying")
    elif age > 10:
        print("You're eligible,boy!")
    else:
        print("Sorry boy! you're not eligible")
elif gender == 'female':
    if age == 12:
        print("you're 1 year away from flying")
    elif age > 12:
        print("You're eligible,girl!")
    else:
        print("Sorry lady! you're not eligible")

#exercise_nestedCondition(aysha).py
#exercise_nestedCondition(nabila).py