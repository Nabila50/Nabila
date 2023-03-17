# Nested Condition:
CGPA = float(input("What is your CGPA?"))
degree = input("Name of your degree")

# eligibility:  degree = Masters and CGPA> 3, Degree = bachelor and CGPA >2

if degree == 'masters':
    if CGPA >= 3:
        print("You are eligible for applying to PhD degree")
    elif CGPA > 3.5:
        print("Congratulation!! you are selected for PhD degree")
    else:
        print("Sorry! You are not selected for PhD degree")
elif degree == 'bachelor':
    if CGPA >= 2:
        print("You are eligible for applying to Masters degree")
    elif CGPA > 3:
        print("Congratulation!! you are selected for Masters degree")
    else:
        print("Sorry! You are not selected for Masters degree")
