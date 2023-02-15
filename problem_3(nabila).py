#3. Write a Python program to construct the following pattern, using a nested for loop:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
for i in range(6):
    print(i*'*')
for j in reversed(range(5)):
    print(j*'*')

