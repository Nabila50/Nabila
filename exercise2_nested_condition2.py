book = int(input("How much book do you buy?:\n"))

if 0 <= book <=5:
    print("There is no offer available for buyers")
elif 5 <= book <=10:
    print("Hey! You got 1 sticker for free")
elif 10 <= book <=15:
    print("Great! You got 1 book for free")
elif 15 <= book <=30:
    print("okay! You got 2 books for free")
else:
    print("Congratulations! You got 20% discount from our shop! Thank You")


