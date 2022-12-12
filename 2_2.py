from sympy import *
import sys
stdout_fileno = sys.stdout

def xgcd(rm2, rm1, ym2, ym1, i):
    
    q0 = quo(rm2, rm1)
    r0 = rem(rm2, rm1)
    y0 = ym2 - ym1 * q0
    
    print(f'#{i+1}\n    r_{{{i-2}}} = r_{{{i-1}}} * q_{{{i}}} + r_{{{i}}}')
    print(f'    r_{{{i}}} =', latex(r0/1), f'\n    q_{{{i}}} =', latex(q0/1))
    print(f'    y_{{{i}}} = y_{{{i-2}}} - y_{{{i-1}}} * q_{{{i}}} =', latex(y0/1))
    
    if r0.degree() == 0:
        return quo(y0, r0)
    
    return xgcd(rm1, r0, ym1, y0, i+1)

x = Symbol('x')

# input coeff mod n, Q, g
# output f
print('Input n:')
n = int(input()) # 5
print('Input Q:')
Q = poly(input(), x, modulus=n) #x**4+x**3-5*x**2+x+3
print('Input g:')
g = poly(input(), x, modulus=n) #x**2+4*x+2


ym2 = poly(0, x, modulus=n)
ym1 = poly(1, x, modulus=n)

sys.stdout = open('out/2_2.txt', 'w')
print(f'All coefficients are mod {n}')
print('#0\n    r_{-2} =', latex(Q/1))
print('    r_{-1} =', latex(g/1))
print('    y_{-2} = 0\n    y_{-1} = 1')

#f = invert(g, Q)
f = xgcd(Q, g, ym2, ym1, 0)

lhs = rem(g*f, Q)
rhs = 1
correct = lhs == rhs
print('Check:', latex(lhs/1), '==', rhs, 'is', correct)

if correct: print('CHECK PASSED!')

print('\nAnswer:', latex(f/1))
print('Invert:', latex(invert(g, Q)/1))

sys.stdout.close()
sys.stdout = stdout_fileno

print('File written')
