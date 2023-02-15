# String

a= 'Nabila Nawshin'

b='1470'            # eitao string bcz jokhn qoutation er moddhe thakbe tokn oita string hoye jabe. number string hoi
                    # 2 vabe..1 quation er moddhe likhle 2. number er aage str(2234) likhle.
print(a)
print(b)

#Loop through the letters in the word "banana":
for x in 'banana':
    print(x)

# String length:
a = 'Nabila Nawshin'            # eikhne space o count hoi tai total lenght hobe 14 ta
print(len(a))

# check string
#Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

#-----------------------------------------------------------------------------------------------------------------------

# Integer
# Integer is a whole number, positive or negative without decimals os unlimited length

x = 147569
y = 147615
z = -1462

print(type(x), x)   # here it is find the type and integer number
print(type(y), y)
print(type(z), z)

#-----------------------------------------------------------------------------------------------------------------------
#Complex
#Complex numbers are written with a "j" as the imaginary part:

x = 3+5j
y = 5j
z = -5j

print(x, type(x))
print(y, type(y))
print(z, type(z))

#-----------------------------------------------------------------------------------------------------------------------

# Float
#Float is a number, positive or negative, containing one or more decimals.

x = 1.1025
y = 1.0697
z = -35.59

print(type(x), x)
print(type(y))
print(type(z))

#-----------------------------------------------------------------------------------------------------------------------


# Random Number
# Python does not have a random() function to make a random number, but Python has a
# -built-in module called random that can be used to make random numbers:

import random

print(random.randrange(1, 10))
#-----------------------------------------------------------------------------------------------------------------------

# conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)  # jekhane intiger cilo x oita k float e concvert korar system

#convert from float to int:
b = int(y)     ## jekhane y float cilo oita k int e concvert korar system

#convert from int to complex:
c = complex(x)   ## jekhane intiger cilo x oita k complex e concvert korar system

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))