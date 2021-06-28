## https://www.acmicpc.net/problem/15649

NM = input().rstrip().split()

N = int(NM[0])
M = int(NM[1])

num_list = []
for i in range(1,N+1):
    num_list.append(i)

from itertools import permutations

pa = list(permutations(num_list, M))

for i in pa :
    s = ""
    for j in i :
        s+=str(j)+" "
    print(s)

