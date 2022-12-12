from sympy import *
import sys
stdout_fileno = sys.stdout

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

print('Input n:')
n = int(input()) #5
print('Input k:')
k = int(input()) #8

sys.stdout = open('out/4_1.txt', 'w')
summ = 0
for i, d in enumerate(divisors(k)):
    if i>0:
        print(' + ', end='')
    print(f'u({d})n^{{{k//d}}}', end='')
    summ += moebius(d) * n ** (k//d)
    
print('\nAnswer:', summ/k)
sys.stdout.close()
sys.stdout = stdout_fileno

print('File written')
