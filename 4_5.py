from sympy import *
import sys
stdout_fileno = sys.stdout

x = Symbol('x')
# input n, Q
# output factors, k

# input n, Q
print('Input n:')
n = int(input()) #5
print('Input Q:')
Q = poly(input(), x, modulus=n)# x^40-1


coeff, factors = Q.factor_list()
ans = []
md = 0
for factor in factors:
    ans += [f'({latex(factor[0]/1)})' + (f'^{{{factor[1]}}}' if factor[1]>1 else '')]
    md = max(md, factor[0].degree())
    
sys.stdout = open('out/4_5.txt', 'w')
print(f'Factors are: {coeff} *', ''.join(ans))

print(f'Minimal field is F_{{{n}}}^{{{md}}} because {md} is max degree of factors')

sys.stdout.close()
sys.stdout = stdout_fileno

print('File written')
