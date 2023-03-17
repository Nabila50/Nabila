# for i in range(1, 10+1, 3):
#     print(i)

# break, continue
# a = 20
# for i in range(10, 30 + 1):
#     if i <= a:
#         print(f"sorry, your age is only {i}, you can to not enter")
#         continue
#     else:
#         print("your age is",i,",welcome to the theatre")

# a = 10
#
# for i in range(1,20):
#     if i == a:
#         print(i)
#         break
#     else: print(i)

a = 10
b = 15

for i in range(1, 20):
    if i == a:
        continue
    elif i == b:
        break
    else:
        print(i)
