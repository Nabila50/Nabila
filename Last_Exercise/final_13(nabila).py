#Write a program to count the number of vowels in a given string.

string = input("give a string: ")

vowel = 0
consonent = 0
for i in string:
    if (i == 'a'or i =='e' or i == 'i'or i == 'o'or  i=='u'):
        vowel = vowel+1
    elif i == '':
        consonent = consonent + 1
    else:
        pass
print(f'vowels are {vowel}')