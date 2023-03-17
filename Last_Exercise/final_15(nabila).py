#Write a program to find the largest and smallest elements in a list.

list1 = [142, 159, 258, 175, 369, 159, 587, 741, 658]

list_length = []
for x in list1:
    list_length.append(len(x))
    print(list_length)
#
#
# list_length = []
#
# for x in list:
#     list_length.append(len(x))
#
# lowest = 100
# highest = 0
#
# for i in list_length:
#     if i >= highest:
#         highest = i
#     if i <= lowest:
        #lowest = i