#15. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
#The sample value of n is 5
#Expected Result: 615

n = int(input('enter your number of n'))

result = n + int(str(n)+str(n)) + int(str(n)+str(n)+str(n))

print(result)