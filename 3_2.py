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

# input coeff mod n, Q, M=[[m00 m01][m10 m11]], s = [s0, s1]
# output M^{-1}
n = 5 #

Q = poly(x**2+3*x+3, x, modulus=n) #
m00 = poly(3*x+4, x, modulus=n) #
m01 = poly(x+2, x, modulus=n) #
m10 = poly(x+3, x, modulus=n) #
m11 = poly(3*x+2, x, modulus=n) #
s0 = poly(1, x, modulus=n) #
s1 = poly(1, x, modulus=n) #

det = rem(m00*m11 - m01*m10, Q)
ym2 = poly(0, x, modulus=n)
ym1 = poly(1, x, modulus=n)
print(f'All coefficients are mod {n}')
print('#0\n    r_{-2} =', latex(Q/1))
print('    r_{-1} =', latex(det/1))
print('    y_{-2} = 0\n    y_{-1} = 1')

det = xgcd(Q, det, ym2, ym1, 0)

newm00 = rem(det*m11, Q)
newm01 = rem(det*-m01, Q)
newm10 = rem(det*-m10, Q)
newm11 = rem(det*m00, Q)

news0 = rem(newm00*s0 + newm01*s1, Q)
news1 = rem(newm10*s0 + newm11*s1, Q)

#TODO: Check if everything is correct
print('\nAnswer: M^{-1}')
print('[', latex(newm00/1).rjust(10), latex(newm01/1).rjust(10), ']')
print('[', latex(newm10/1).rjust(10), latex(newm11/1).rjust(10), ']')

print('\nAnswer: M^{-1} * s')
print('[', latex(news0/1).rjust(10), ']')
print('[', latex(news1/1).rjust(10), ']')

