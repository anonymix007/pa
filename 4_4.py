from sympy import *
x = Symbol('x')
# input n
# output m, k

n = 5 #

p = 2 # binary code

print(f'Consider x^{{{n}}}, find its factorization under F_{{{p}}}')

orbits = set()
idx = 0
for i in range(n):
    num = (i*2) % n
    orbit = set([i])
    while num not in orbit:
        orbit.add(num)
        num = (num*p)%n
    orbit = tuple(orbit)
    orbits.add(orbit)
    
print('Orbits are:', orbits)

for orbit in orbits:
    m = len(orbit)
    k = n - m
    print(f'    m = {m}, k = {k}')
    