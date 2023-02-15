#9. Count the number of vowels and consonants in a given string.

word = input('write a word')

vowel= 0
consonent= 0

for i in word:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        vowel=vowel+1
   # elif i == '':
    else:
        consonent=consonent+1

print(f" vowels are {vowel}")
print(f"consonnts are {consonent}")