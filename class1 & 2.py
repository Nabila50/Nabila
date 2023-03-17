print("hello ali!")
print('my name is aysha akter')
print(f"my husband name is ali. he is {30} years old. since {2021} he has been living in germany.")
print("my husband's name is ali", "he is 30 years old", "since 2021 he has been living in germany")
#add
print(20+30+200+380)
#sub
print((3983-383),(38-8))
#mult
print(4*5, 3*2, 20//5, 6*6, 55-5)
#div
print(54/6, 500/10, 120/12)
#divided without extension
print(54//6, 500//10, 120//12)
#power
print(5**2, 4**3, 5**3)
#bracket
print((5-3)*3*(2+1-2)**2)
print((8-3)**3, (4+2-1)//5)
print(2**(6//2))


#other my works
print("200 is a great number")
print(f"20 days are {20 * 24 * 60} minutes")
print(f"20 days are {20 * 24 * 60 * 60} seconds")
print(f"35 days are {35 * 24 * 60} minutes")
print(f"35 days are {35 * 24 * 60 * 60} seconds")
###
calculation_to_units = 24 * 60
name_of_units = "minutes"
print(f"20 days are {20 * calculation_to_units} {name_of_units}")
print(f"35 days are {35 * calculation_to_units} {name_of_units}")
print(f"50 days are {50 * calculation_to_units} {name_of_units}")
print(f"120 days are {120 * calculation_to_units} {name_of_units}")

###
calculation_to_units = 24
name_of_units = "hours"
print(f"20 days are {20 * calculation_to_units} {name_of_units}")
print(f"35 days are {35 * calculation_to_units} {name_of_units}")
print(f"50 days are {50 * calculation_to_units} {name_of_units}")
print(f"120 days are {120 * calculation_to_units} {name_of_units}")

def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}")

days_to_units(20)
days_to_units(35)
days_to_units(50)
days_to_units(120)

###
x = 24 * 60
y = "minutes"
def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * x} {y}")

days_to_units(10)
days_to_units(55)
days_to_units(5)
days_to_units(7)


###
x = 24
y = "hours"
print(f"20 days are {20 * x} {y}")

#class 2 #######################

print("my husband is ",35, "years old")
print("my father is {age} years old".format(age=50))

print("my father is {age} years old".format(age=60))

print("{a} + {b} = {c}".format(a=25,b=15, c=40))

a = 20
b = 10

c = "germany"

print(a*b)
print(a//b)
print(c*a) # str and int er multiple korle str int er soman hobe
print(a*c) # int and str er multiple korle str int er soman hobe
#print(b+c) # str and int er jog korle error asbe
print(c,b) # evabe str and int jog kora jabe

# conversion to integer

a = input()  # a=5
b = input()  # a=7

c = a+b

d = int(a)  # int 5
e = int(b)  # int 7

f = d+e

print(a, b)  # 5 7
print(c)  # 57
print(d, e)  # 5 7
print(f)  # 12

# conversion to float

a = input()  # a=5
b = input()  # a=7

c = a+b

d = float(a)  # int 5
e = float(b)  # int 7

f = d+e

print(a, b)  # 5 7
print(c)  # 57
print(d, e)  # 5 7
print(f)  # 12

# calculator

a = int(input())
b = int(input())

print(f"the addition of {a} and {b} = {a+b}")
print(f"the subtraction of {a} and {b} = {a-b}")
print(f"the multiple of {a} and {b} = {a*b}")
print(f"the division of {a} by {b} = {a/b}")
print(f"the division  of {a} by {b} (without extension) = {a//b}")
print(f" {a} to the power {b} = {a**b}")
#print(f"the addition of {a} and {b} = {a+b}")

## Class 3 & 4

temperature = -40

if temperature > 30:
    print("its warm")
    print("drink water")
elif temperature < -20:
    print("its too cold")
else:
    print("its normal")

a = int(input())

if a >= 20:
    print(f"{a} is greater than 20")
    print(f"{a} is greater or equal to 20")
elif a <= 5:
    print(f"{a} is less than 5")
    print(f"{a} is equal to 5")
else:
    print("nothing")

a = int(input())
if a == 20:
    print(f"{a} is not greater than 20")
    print(f"{a} is equal to 20")
elif a != 5:
    print(f"{a} is less than 5")
    print(f"{a} is not equal to 5")
else:
    print("all")


####   SUHAG

print("my name is",30+2, "old age")
print("{a} + {b}={c}".format(a=5,b=5,c=5+5))
a=int(input())
b=int(input())
print(f"the addition {a} and {b}={a+b}")