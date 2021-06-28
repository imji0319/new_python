## https://www.acmicpc.net/problem/2798



import sys

N_M = sys.stdin.readline().rstrip().split()
M = int(N_M[1])
num_list = sys.stdin.readline().rstrip().split()


sum = 0

for f in num_list:
    for s in num_list[1:]:
        for t in num_list[2:]:
            if f != s and s != t and f !=t:
                tst = int(f)+int(s)+int(t)

            if tst > sum and tst <= M:
                sum = tst

print(sum)



