## https://www.acmicpc.net/problem/1316



import sys

nums = int(sys.stdin.readline())

group_word = []
for i in range(nums):
    st = sys.stdin.readline().rstrip()
    group_word.append(st)


n = 0
for i in group_word:
    breaker = False
    stt = []

    for j in i :
        #print(i, j)
        if stt and stt[-1] != j :
            if j in stt:
                breaker = True
        stt.append(j)

    #print(stt, breaker)
    if breaker == False:
        n+=1


print(n)


