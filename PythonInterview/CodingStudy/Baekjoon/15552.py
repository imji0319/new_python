## https://www.acmicpc.net/problem/15552


import sys

st = ""

ss = sys.stdin.readline()
for i in range(int(ss)):
    s = sys.stdin.readline().rstrip().split()
    print(int(s[0])+int(s[1]))

