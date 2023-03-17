
#11. Print all prime numbers from 1 to 100.

for i in range(1, 101):
    is_prime= True

    for x in range(2, i):
        if i % x==0:
            is_prime = False
            break
        else:
            pass
    if is_prime:
        print(i, ': is a prime number')
    else:
        pass

