from copy import deepcopy
from pprint import pprint
n= int(input("n: "))
x= int(input("x: "))

M = []

for i in range(n):
    row = []
    for j in range(n):
        if (i==0) or (j==0):
            row = row +[x]
        else:
            row = row + [row[j-1] + M[i-1][j]]
    M = M + [row]
 
pprint(M)