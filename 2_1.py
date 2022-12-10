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

# input coeff mod n, poly degree m, simplified g, w, h
# output f
n = 7 #

F = FiniteField(n)

h = poly(6*x**3+x**2+3, x, domain=F) #
g = rem(poly(2*x**3+6*x**2+4*x+5, x, domain=F), h) #
w = poly(5*x+4, x, domain=F) #
ym2 = poly(0, x, domain=F)
ym1 = poly(1, x, domain=F)

print('#0\n    r_{-2} =', h)
print('    r_{-1} =', g)
print('    y_{-2} = 0\n    y_{-1} = 1')

#f = rem(invert(g, h)*w, h)
f = rem(xgcd(h, g, ym2, ym1, 0) * w, h)

lhs = rem(g*f, h)
rhs = w
correct = lhs == rhs
print('Check:', lhs, '==', rhs, 'is', correct)

if correct: print('CHECK PASSED!')

print('\nAnswer: f(x) =', f)
