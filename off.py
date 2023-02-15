tries = int(input("How many times do you want to try?"))

import random

number = random.randint(1, 50)
print(number)

for i in range(tries):
    guess = int(input("Enter Your guess number:"))
    if (guess - number) <= -5:
        print("Your guess is low but closer")
    elif -6 >= (guess - number) >= -10:
        print("Your guess is little bit low")
    elif -11 >= (guess - number) >= -15:
        print("Your guess is very lower ")
    elif -16 >= (guess - number) >= -20:
        print("Your guess is so much lower")
    elif -21 >= (guess - number) >= -25:
        print("Your guess very far away than the guess number")
    elif 0 <= (guess-number) <= 5:
        print("Your guess is not right but close to number")
    elif 6 <= (guess-number) <= 10:
        print("Your guess is close to number")
    elif 11 <= (guess-number) <= 15:
        print("Your guess is higher than the number")
    elif 16 <= (guess-number) <= 20:
        print("Your guess is very higher than the number")
    elif 21 <= (guess-number) <= 25:
        print("Your guess is so much higher than the number")


    elif guess == number:
        print("Yeah! You are done for now!")
        break