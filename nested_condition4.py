gender = input("what's your gender?")
age = int(input("what's your age?"))
salary = int(input("what's your salary in BDT?"))

if gender == 'man' and (age >= 18 or salary >= 30000):
    print("abcd")
else:
    print('not abcd')