

from typing import List
import collections
import heapq

def DelayTime(times : List[List[int]], N : int, K : int ):

    graph = collections.defaultdict(list)

    for u, v, w in times :
        graph[u].append((v,w))

    # 우선순위 큐 정의 [ (소요시간, 정점) ]
    Q = [(0, K)]
    dist = collections.defaultdict(int)

    # 우선 순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입 
    while Q :
        time, node = heapq.heappop(Q)

        if node not in dist :
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))

