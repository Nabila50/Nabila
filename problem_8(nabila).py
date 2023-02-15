#8. Check if a given string is a palindrome.

text = input('write a text:')

if text == text[::-1]:                    # forward and backward print korar system print[text, text::-1]
    print('this is a palindrome string')
else:
    print('this is not a palindrome string')