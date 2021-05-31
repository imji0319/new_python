
### https://www.acmicpc.net/problem/14954

import collections

def solution(n) -> bool:

    square_list = []

    def dfs(num):
        s = 0
        for i in str(num):
            s += int(i)**2

        #print(s)
        if s in square_list:
            #print('UNHAPPY')
            return False

        if s == 1:
            #print('HAPPY')
            return True

        square_list.append(s)
        return dfs(s)

    result = dfs(n)

    if result :
        print('HAPPY')
    else:
        print('UNHAPPY')

solution(21)
solution(19)
solution(5)