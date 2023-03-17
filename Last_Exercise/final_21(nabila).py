#Write a program to remove the nth element from a list.

n = [1, 2, 6, 7, 6, 9, 2, 8]

list_1 = 0


nth = int(input("Enter the nth element: "))
n.pop(nth-1)
print(n)


