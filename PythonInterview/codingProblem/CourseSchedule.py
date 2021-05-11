'''
0 을 완료하기 위해서는 1을 끝내야 하는 것을 [0,1] 쌍으로 표현하는 n개의 코스가 있다. 코스의 개수 n과 이 쌍들을 입력으로 받았을 때
모든 코스가 완료 가능한지 판별
'''

from typing import List
import collections

def canFinish(numCourse : int, prerequisites : List[List[int]]) -> bool:
    graph = collections.defaultdict(list)

    for x, y in prerequisites:
        graph[x].append(y)

    traced = set()

    def dfs(i):
        # 순환구조면 False
        if i in traced :
            return False

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False

        # 탐색 종료 후 순환 노드 삭제
        traced.remove(i)

        return True

    # 순환 구조 판별
    for x in list(graph):
        if not dfs(x):
            return False

    return True


print(canFinish(2, [[1,0], [0,2],[1,2]]))

def canFinish2(numCourse : int, prerequisites : List[List[int]]) -> bool :
    graph = collections.defaultdict(list)

    for a, b in prerequisites:
        graph[a].append(b)

    traced = set()
    visited = set()

    def dfs(i):
        # 순환 구조이면 False
        if i in traced :
            return False

        # 이미 방문했던 노드이면 False
        if i in visited :
            return False

        traced.add(i)

        for y in graph[i]:
            if not dfs(y):
                return False

        # 탐색 종료 후 순환 노드 삭제
        traced.remove(i)
        # 탐색 종료 후 방문 노드 추가
        visited.add(i)

        return True


    # 순환 구조 판별
    for x in list(graph):
        if not dfs(x):
            return False

    return True




