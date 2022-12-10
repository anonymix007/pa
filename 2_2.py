from sympy import *


def xgcd(rm2, rm1, ym2, ym1, i):
    
    q0 = quo(rm2, rm1)
    r0 = rem(rm2, rm1)
    y0 = ym2 - ym1 * q0
    
    print(f'#{i+1}\n    r_{{{i-2}}} = r_{{{i-1}}} * q_{{{i}}} + r_{{{i}}}')
    print(f'    r_{{{i}}} =', r0, f'\n    q_{{{i}}} =', q0)
    print(f'    y_{{{i}}} = y_{{{i-2}}} - y_{{{i-1}}} * q_{{{i}}} =', y0)
    
    if r0.degree() == 0:
        return quo(y0, r0)
    
    return xgcd(rm1, r0, ym1, y0, i+1)

x = Symbol('x')

# input coeff mod n, Q, g
# output f
n = 5 #

F = FiniteField(n)

Q = poly(x**4+x**3-5*x**2+x+3, x, domain=F) #
g = poly(x**2+4*x+2, x, domain=F) #
ym2 = poly(0, x, domain=F)
ym1 = poly(1, x, domain=F)
print('#0\n    r_{-2} =', Q)
print('    r_{-1} =', g)
print('    y_{-2} = 0\n    y_{-1} = 1')

#f = invert(g, Q)
f = xgcd(Q, g, ym2, ym1, 0)

lhs = rem(g*f, Q)
rhs = 1
correct = lhs == rhs
print('Check:', lhs, '==', rhs, 'is', correct)

if correct: print('CHECK PASSED!')

print('\nAnswer:', f)
