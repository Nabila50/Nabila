#4. Write a Python program to count the number of even and odd numbers from a series of numbers.

even = 0
odd = 0

for i in range(1, 50):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"odd numbers:{odd}, even numbers:{even}")