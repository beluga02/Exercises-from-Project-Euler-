import math


def largest_prime_factor(n):
    var = 0
    lista = []
    for i in range(1, int(math.sqrt(n))):
        j = 0
        if n % i == 0:
            var = i
            while j < 2:
                for k in range(1, var+1):
                    if var % k == 0:
                        j += 1
            if j == 2:
                lista.append(var)
    return max(lista)


n = 600851475143
print(largest_prime_factor(n))
