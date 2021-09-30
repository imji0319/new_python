### https://www.acmicpc.net/problem/12846
### https://www.acmicpc.net/board/view/62126

import sys
num = int(input())
T = list(map(int, sys.stdin.readline().split()))


answer = 0
stack = []

for i in range(1, num):
    print(stack)
    right = i - 1
    while stack and T[stack[-1]] > T[i]:
        temp = stack.pop()

        left = 1 if len(stack) == 0 else stack[-1] + 1
        answer = max(answer, T[temp] * (right - left + 1))
    stack.append(i)

right = len(T)-1
while stack:
    temp = stack.pop()
    left = 1 if len(stack) == 0 else stack[-1] + 1
    answer = max(answer, T[temp]*(right - left + 1))


print(answer)
