# K 번 이상 등장하는 요소 추출
'''
상위 K순위까지가 아닌 값 요소의 개수가 K번 이상임을 찾아야 되는 문제일 경우
책에 나온 방식대로 진행할 경우 최대 K개의 숫자만 추출됨.
만약 K번 이상 등장하는 요소가 3개 이상일 경우 해결할 수 없음.
'''

from typing import List
import collections
import heapq

def solution(nums : List[int], k : int) -> List[int]:

    freq = collections.Counter(nums)
    #print(freq)
    topk = []
    for i in freq:
        if freq[i] >= k:
            topk.append(i)

        #print(i, freq[i])

    return sorted(topk)



print(solution([1,4,4,1,1,2,2,5], 2))