# Write a program to count the number of words in a given string.

string =  input('give some words')
# a= string.split(' ')
# print(len(a))



# other way has some problme.------------------------------------------
value = 0
for i in string:
    if value == i.split(' '):
        value = value+ 1
    print(value)
else:
    len(value)
    print(f'given string is {value}')