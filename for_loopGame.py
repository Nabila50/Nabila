# name : Guess the number
# how many tries do you want?
# he will enter a number (enter a number between 1 - 50)
# if number>5 : you're little bit higher
# if number>10 : you're very high
# if number<5 : you're little bit lower
# if number<10 : you're very low

import random

tries = int(input('How many tries do you want?'))
number = random.randint(1, 50)
print(number)

print('Guess a number between 1 to 50')
for i in range(tries):
    guess = int(input("Enter your guess:"))

    if guess == number:
        print('Your guess is RIGHT!')
        break

    elif (guess-number)>10:
        print("you're very high")
    elif 10 > (guess - number) > 5:
        print("you're little bit high")
    elif (guess-number) < (-10):
        print("you're very low")
    elif (-10) < (guess - number) < (-5):
        # 42-50 = -8 < -10 and 42-50 = -8 > -5
        print("you're little bit low")

