### https://www.acmicpc.net/problem/12846

#import sys
#sys.setrecursionlimit(10**6)


num = int(input())
T = list(map(int, input().split()))

stack = []
restack =[]
answer = [1] * len(T)
for i, cur in enumerate(T):
    #print(i, stack,restack)

    if stack and cur >= T[stack[-1]]:
        restack = stack.copy()
        while restack:
            last = restack.pop()
            answer[last] += 1
            #print('answer', answer)

    elif stack and cur < T[stack[-1]]:
        restack = stack.copy()
        while restack:
            last = restack.pop()
            #print(last)
            if T[last] <= cur:
                answer[last] += 1
                #print(answer)


    stack.append(i)

#print('answer')
#print(answer)

print(max([answer[i] * T[i] for i in range(num)]))

