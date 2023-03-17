# is_student = bool(input("Are you a student?:\n"))
grade = int(input("In which class do you read in? :\n"))
score = float(input("what's your score?:\n"))

# print(is_student, grade, score)

# if is_student:
#     print("he is a student")
# else:
#     print("he is not a student")

if grade == 2 and score >= 50:
    print('You can have this ice cream')
elif grade >= 5 or score >= 90:
    print('You are good to have this tshirt')
else:
    print('condition not matched')
