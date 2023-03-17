# list Accessing:

flowers = ["Rose", 'sunflowers', 'camelia', 'rajonigandha', 'gladiolus', 'zarbera', 'goldmerry', 'joba', 'sokal sondha']

# total koita information ace ta ber korar code----------------
#print(len(flowers))

# Alfabet hisabe asbe------------------------------------------
#print(sorted(flowers))

# Reverse hisab asbe-------------------------------------------
#print(sorted(flowers, reverse=True))

#--------------------------------------------------------------
#for numbers

numbers = [10, 3, 17, 20, 39, 16, 22, 83, 71, 16, 901, 87, 49, 55, 1, 34, 66, 14]
print(len(numbers))
print(sorted(numbers))
print(sorted(numbers, reverse=True))

#--------------------------------------------------------------

mixed = ['orange', 14.5, 'banana', True, 78.7, 'Kiwi', 1.79, 'cherry', True, 7.34, False, 4, 'mango', 3.47]
print(len(mixed))
# print(sorted(mixed))            # it will not give the information

#-----------------------------------------------------------------------------------
animal = ['cat', 'lion', 'goat', 'dog', 'sheep', 'horse', 'rabbit', 'tiger', 'dear']
print(animal[0])   # eikhane cat asbe cz cat er position 0, lion=1, goat=2, dog=3, sheep=4, horse=5, rabbit=6, tiger=7, dear=8
print(animal[1])
print(animal[6])
print(animal[-1])       # eikhne reverse information ase -1 = dear
print(animal[-4])       # eikhne reverse information ase -4 = horse

print(animal[0:3])      # here print start from 1 to 3 = cat to goat
print(animal[0:5:2])    # ekta bade ekta ekta print hobe
print(animal[3:7])      # dog theke rabbit porjont print korar system
print(animal[-4:-1])    # horse theke tiger porjont print korar system
print(animal[2:])       # position 2 theke baki sob gula print korar system---goat theke dear porjonto full print hobe
print(animal[::-1])     # Reverse theke print korar system
print(animal[4::-1])    # Reverse position 4= sheep theke samner dike position 0=cat porjonto reverse print korar system
print(animal[:3:-1])    # postion 3=dog er aag porjonto reverse e print korar system
print(animal[6:2:-1])   # Reverse theke rabbit to dog porjonto print er system where position 6=rabbit and 2=goat
print(animal[7:4:-1])   #  Reverse theke tiger to horse porjonto print er system where position 7=tiger and 4= sheep
