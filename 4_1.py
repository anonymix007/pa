from sympy import *


def moebius(x):
    if x==1:
        return 1
    factors = factorint(x)
    res = 1
    for factor, cnt in factors.items():
        if cnt > 1:
            return 0
        res *= -1
    return res
        
# input n, k

n = 5 #
k = 8 #

sum = 0
for i, d in enumerate(divisors(k)):
    if i>0:
        print(' + ', end='')
    print(f'u({d})n^{{{k//d}}}', end='')
    sum += moebius(d) * n ** (k//d)
    
print('\nAnswer:', sum/k)