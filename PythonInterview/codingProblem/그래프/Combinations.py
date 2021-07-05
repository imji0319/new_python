# 전체 수 n을 입력받아 k개의 조합을 리턴하라.

from typing import List

def combine(n : int , k : int) -> List[List[int]]:
    results = []

    def dfs(elements, start : int, k : int):
        if k == 0 :
            results.append(elements[:])

        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i+1, k-1)
            elements.pop()
    dfs([], 1, k)

    return(results)


print(combine(4,2))


import itertools

def combine2(n : int, k : int) -> List[List[int]]:
    return list(itertools.combinations(range(1, n+1), k))