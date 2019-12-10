import numpy as np
li = np.random.randint(-100, 100, size=100)
print('Original list', li)
 #Q.a
posli = list(map(lambda x: x if x >=0 else -x,li))
print('Positive list',posli)

def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
#.b
primes = list(filter(is_prime,posli))
print('Primes:',primes)
#.c
for p in primes:
    divisible = list(filter(lambda x: x % p == 0, posli))
    print(p, ':', divisible)