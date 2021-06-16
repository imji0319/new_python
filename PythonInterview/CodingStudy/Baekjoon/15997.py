## https://www.acmicpc.net/problem/15997

import sys

teams = sys.stdin.readline().rstrip().split()
teams = dict.fromkeys(teams, 0)
#print(teams)
for i in range(6):
    case = sys.stdin.readline().rstrip().split()
    A = case.pop(0)
    B = case.pop(0)

    case = list(map(float, case))

    teams[A] += case[0]*3 + case[1]*1 # 기댓값
    teams[B] += case[1]*1 + case[2]*3 # 기댓값


print(teams)

from collections import Counter

c = Counter(teams.values())
idv = {key: rank for rank, key in enumerate(sorted(c, reverse =True))}
#print(c) # 점수 개수
#print(idv) # 점수 순위
for k, v in teams.items():
    teams[k] = idv[v]

c1 = Counter(teams.values())
#print(c1)
#print(teams)


for k, v in teams.items():
    if v == 0 and c1[v] == 1 :
        teams[k] = 1
    elif v == 0 and c1[v] != 1 :
        teams[k] = 1/c1[v]
    elif v == 1 and c1[v] == 1:
        teams[k] = 1
    elif v == 1 and c1[v] != 1:
        teams[k] = 1/c1[v]
    else :
        teams[k] = 0

for k , v in teams.items():
    print(v)