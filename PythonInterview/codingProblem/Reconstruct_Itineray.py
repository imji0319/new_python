
'''
[from , to]로 구성된 항공권 목록을 이용해 JFK에서 출발하는 여행 일정을 구성하라.
여러 일정이 있는 경우 사전 어휘 순으로 방문
'''
from typing import List
import collections

def ReconstructItinerary(tickets : List[List[str]]) -> List[str] :

    graph = collections.defaultdict(list)
    for a, b in sorted(tickets):
        graph[a].append(b)
    route = []


    def dfs(a):
        # 첫번째 값을 읽어 어휘 순으로 방문
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)

    dfs('JFK')

    # 다시 뒤집어 어휘순 결과로
    return route[::-1]

tickets = [['JFK','SFO'],['JFK','ATL'],['SFO','ATL'],['ATL','JFK'],['ATL','SFO']]
print(ReconstructItinerary(tickets))



def FindItinerary(tickets : List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)
    for a, b in sorted(tickets, reverse = True ):
        graph[a].append(b)

    route = []

    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop())
        route.append(a)

    dfs('JFK')
    return route[::-1]

print(FindItinerary(tickets))


def FindItinerary2(tickets : List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)

    for a, b in sorted(tickets):
        graph[a].append(b)

    route, stack =[],['JFK']

    while stack :
        # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())

    return route[::-1]

print(FindItinerary2(tickets))

