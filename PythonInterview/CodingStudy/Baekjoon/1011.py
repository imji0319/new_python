## https://www.acmicpc.net/problem/1011


import sys

n = sys.stdin.readline()

test = []
for i in range(int(n)):
    s = sys.stdin.readline().rstrip().split()

    test.append(s)

print(test)

for i in range(int(n)):
    x = int(test[i][0])
    y = int(test[i][1])

    c = y - x
    s =  0
    n = 1
    while s < c :
        s += 2*n
        n += 1

    print(s, n)

                      





