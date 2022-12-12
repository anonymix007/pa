from sympy import *
import sys
stdout_fileno = sys.stdout


# input n, m, G
# output d

#'''

print('Input m:')
m = int(input()) #3
print('Input n:')
n = int(input()) #6
print('Input H (m rows, n cols) row by row:')
G = Matrix([[int(x) for x in input().split(' ')] for y in range(n)])
#G = Matrix([[1,1,1],[1,1,1,],[1,0,1],[0,0,0],[0,0,1],[0,0,0]]) #
'''

#'''

V = Matrix()
for v in range(1, 2**m):
    s = format(v, f'0{m}b')
    
    col = [ord(c)-ord('0') for c in s]
    V = V.col_insert(v-1, Matrix(col))

sys.stdout = open('out/6_3.txt', 'w')
print('Matrix of possible to-be-encoded words V:')
pprint(V)
print('G * V:')
A = (G * V) % 2
pprint(A)

ds = [sum(A.col(col)) for col in range(A.shape[1])]
print('', '  '.join([str(d) for d in ds]))
print(f'\nAnswer: distance is {min(ds)}')

sys.stdout.close()
sys.stdout = stdout_fileno

print('File written')
