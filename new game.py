tries = int(input("How many times do you want to try?"))

import random

number = random.randint(1, 500)

for i in range(tries):
    guess = int(input("Enter Your guess number:"))
    if (guess - number) >= -50:
        print("Your guess is low but closer")
    elif -51 > (guess - number) >= -100:
        print("Your guess is little bit low")
    elif -101 > (guess - number) >= -150:
        print("Your guess is very lower ")
    elif -151 > (guess - number) >= -200:
        print("Your guess is so much lower")
    elif -201 > (guess - number) >= -250:
        print("Your guess very far away than the guess number")
    elif (guess-number) <= 50:
        print("Your guess is not right but close to number")
    elif 51 < (guess-number) <= 100:
        print("Your guess is close to number")
    elif 101 < (guess-number) <= 150:
        print("Your guess is higher than the number")
    elif 151 < (guess-number) <= 200:
        print("Your guess is very higher than the number")
    elif 201 < (guess-number) <= 250:
        print("Your guess is so much higher than the number")


    elif guess == number:
        print("Yeah! You are done for now!")
        break