#Write a program to find the average of elements in a list.

list1= [1, 6, 7, 9, 3, 4]

summation = sum(list1)
length = len(list1)

average = summation / length
print(f'average of elemenst in a list is {average}')


# other way to solve the problem in for loop

average = 0
for i in list1:
    average += i
print(average/len(list1))
#print(f'average of elemenst in a list is {average/len(list1)}')