from sympy import *
import sys
stdout_fileno = sys.stdout
# input m, n, H, u1, u2
# output v1, v2 ( = encoded u1, u2)

#'''
print('Input m:')
m = int(input()) #7
print('Input n:')
n = int(input()) #3
print('Input H (m rows, n cols) row by row:')
H = Matrix([[int(x) for x in input().split(' ')] for y in range(n)])
#H = Matrix([[0,1,1,1,0,0,0],[0,1,0,1,0,1,0],[1,0,1,0,0,1,1]]) #
print('Input vector u1:')
u1 = Matrix([int(input()) for x in range (m-n)]) # 1 1 0 0
print('Input vector u1:')
u2 = Matrix([int(input()) for x in range (m-n)]) # 1 1 1 0
'''

#'''
sys.stdout = open('out/6_2.txt', 'w')
RREF, pivot = H.rref(iszerofunc=lambda x: x % 2 == 0)
#print(f'Code is ({m}, {n}), so {m} bits in encoded words, {n} bits in to-be-coded words')
RREF%=2
print('Row reduced:')
pprint(RREF)
#print(pivot)
assert(pivot == tuple(range(n)))

G = Matrix(RREF)
for _ in range(n):
    G.col_del(0)
#pprint(G)
#print(G.shape)

I44 = eye(m-n)
#pprint(I44)
for i in range(m-n):
    G = G.row_insert(n+i, I44.row(i))

print('Generating matrix:')
pprint(G)

pprint(u1.T)
pprint(u2.T)

v1 = (G * u1) % 2
v2 = (G * u2) % 2
print('\nAnswer: \nEncoded u_{1}^{T} is:')
pprint(v1.T)
print('Encoded u_{2}^{T} is:')
pprint(v2.T)

sys.stdout.close()
sys.stdout = stdout_fileno

print('File written')
