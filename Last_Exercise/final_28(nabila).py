#Write a program to create a dictionary from two lists.

color = ['white', 'yellow', 'red', 'black', 'blue', 'sky blue']
number = [1, 2, 9, 8, 7, 6]

# Keys = color.key(color)
# value = number.values(number)
#
# dictionary = dict(Keys, value)
# print(dictionary)

de = {}

for i in color:
    de.update(i)
    print(de)
