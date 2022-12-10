from sympy import *


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

# input coeff mod n, Q, M=[[a b][c d]]
# output M^{-1}
n = 5 #

Q = poly(x**2+3*x+3, x, modulus=n) #
a = poly(3*x+4, x, modulus=n) #
b = poly(x+2, x, modulus=n) #
c = poly(x+3, x, modulus=n) #
d = poly(3*x+2, x, modulus=n) #

det = rem(a*d - b*c, Q)
ym2 = poly(0, x, modulus=n)
ym1 = poly(1, x, modulus=n)
print(f'All coefficients are mod {n}')
print('#0\n    r_{-2} =', latex(Q/1))
print('    r_{-1} =', latex(det/1))
print('    y_{-2} = 0\n    y_{-1} = 1')

det = xgcd(Q, det, ym2, ym1, 0)

newa = rem(det*d, Q)
newb = rem(det*-b, Q)
newc = rem(det*-c, Q)
newd = rem(det*a, Q)

#TODO: Check if everything is correct
print('\nAnswer:')
print('[', latex(newa/1).rjust(10), latex(newb/1).rjust(10), ']')
print('[', latex(newc/1).rjust(10), latex(newd/1).rjust(10), ']')

