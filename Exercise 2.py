import math


def fibonacci():
    f = 1
    s = 2
    soma = 2
    n = 0
    while n <= 4000000:
        n = f + s
        f = s
        s = n
        if n % 2 == 0:
            soma += n
    return soma


print(fibonacci())
