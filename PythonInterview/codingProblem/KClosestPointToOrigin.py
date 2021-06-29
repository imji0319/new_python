
import math
import heapq

def solution(points, K):

    #zeropoint = [0,0]
    heap = []
    for x,y in points :
        ss = math.sqrt((x-0)**2 + (y-0)**2)
        heapq.heappush(heap, (ss, x, y)) # 작은 순서대로 저장


    result = []

    for _ in range(K):
        (dist, x, y) = heapq.heappop(heap) # 맨앞부터 pop
        result.append((x,y))

    return result





