## https://www.acmicpc.net/problem/4344


import sys

test_case = sys.stdin.readline()

for i in range(int(test_case)):
    case = sys.stdin.readline().rstrip().split()
    sums = 0
    map_int = list(map(int, case))
    c = map_int.pop(0)

    for i in map_int:
        sums += i


    mean = sums/c
    #print(mean)

    y = len([i for i in map_int if i > mean])
    print('%.3f%%' %(y/c * 100))





