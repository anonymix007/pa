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

# input coeff mod n, Q, M=[[m00 m01][m10 m11]], s = [s0, s1]
# output M^{-1}
n = 5 #

F = FiniteField(n)

Q = poly(x**2+3*x+3, x, domain=F) #
m00 = poly(3*x+4, x, domain=F) #
m01 = poly(x+2, x, domain=F) #
m10 = poly(x+3, x, domain=F) #
m11 = poly(3*x+2, x, domain=F) #
s0 = poly(1, x, domain=F) #
s1 = poly(1, x, domain=F) #

det = rem(m00*m11 - m01*m10, Q)
ym2 = poly(0, x, domain=F)
ym1 = poly(1, x, domain=F)
print('#0\n    r_{-2} =', Q)
print('    r_{-1} =', det)
print('    y_{-2} = 0\n    y_{-1} = 1')

#f = invert(g, Q)
det = xgcd(Q, det, ym2, ym1, 0)

newm00 = rem(det*m11, Q)
newm01 = rem(det*-m01, Q)
newm10 = rem(det*-m10, Q)
newm11 = rem(det*m00, Q)

news0 = rem(newm00*s0 + newm01*s1, Q)
news1 = rem(newm10*s0 + newm11*s1, Q)

#lhs = rem(g*f, Q)
#rhs = 1
#correct = lhs == rhs
#print('Check:', lhs, '==', rhs, 'is', correct)

#if correct: print('CHECK PASSED!')

print('\nAnswer: M^{-1}')
print('[', newm00, newm01, ']')
print('[', newm10, newm11, ']')

print('\nAnswer: M^{-1} * s')
print('[', news0, ']')
print('[', news1, ']')

