from sympy import *
import sys
stdout_fileno = sys.stdout

x = Symbol('x')
# input n, Q
print('Input n:')
n = int(input()) #2
print('Input Q:')
Q = poly(input(), x, modulus=n)# x^11+x^9+x^8+x^4+x^3+x^2+1

sys.stdout = open('out/4_3.txt', 'w')

roots = Q.ground_roots()
print('Roots are:', roots)

coeff, factors = Q.factor_list()
ans = []
for factor in factors:
    ans += [f'({latex(factor[0]/1)})' + (f'^{{{factor[1]}}}' if factor[1]>1 else '')]

print(f'Factors are: {coeff} *', ''.join(ans))
sys.stdout.close()
sys.stdout = stdout_fileno

print('File written')
