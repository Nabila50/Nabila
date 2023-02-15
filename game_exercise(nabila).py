tries = int(input("How many times do you want to try?"))

import random

number = random.randint(1, 50)

for i in range(tries):
    guess = int(input("Enter Your guess number:"))
    if (guess - number) <= -5: #0-5 =-5
        print("Your guess is very low")
    elif 16 < (guess - number) <= 26: #18-15= 3
        print("Your guess is little bit low")
    elif 21 < (guess - number) <= 30:
        print("Your guess is little bit high")
    elif 31 < (guess - number) <= 40:
        print("Your guess is more little bit high")
    elif 41 <= (guess - number) <= 50:
        print("Your guess is very high")
    elif guess == number:
        print("Yeah! You are done for now!")
        break