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

# input coeff mod n, Q, M=[[a b][c d]]
# output M^{-1}
n = 5 #

F = FiniteField(n)

Q = poly(x**2+3*x+3, x, domain=F) #
a = poly(3*x+4, x, domain=F) #
b = poly(x+2, x, domain=F) #
c = poly(x+3, x, domain=F) #
d = poly(3*x+2, x, domain=F) #

det = rem(a*d - b*c, Q)
ym2 = poly(0, x, domain=F)
ym1 = poly(1, x, domain=F)
print('#0\n    r_{-2} =', Q)
print('    r_{-1} =', det)
print('    y_{-2} = 0\n    y_{-1} = 1')

#f = invert(g, Q)
det = xgcd(Q, det, ym2, ym1, 0)

newa = rem(det*d, Q)
newb = rem(det*-b, Q)
newc = rem(det*-c, Q)
newd = rem(det*a, Q)

#lhs = rem(g*f, Q)
#rhs = 1
#correct = lhs == rhs
#print('Check:', lhs, '==', rhs, 'is', correct)

#if correct: print('CHECK PASSED!')

print('\nAnswer:')
print('[', newa, newb, ']')
print('[', newc, newd, ']')

