import heapq
from typing import List
import collections

def topKFrequent(nums : List[int], k : int) -> int :
    n = collections.Counter(nums)
    print(sorted(n)[k-1])


def findKthLargest(nums :List[int], k : int) -> int:
    heap = list()
    for n in nums:
        heapq.heappush(heap, -n)

    for _ in range(k):
        heapq.heappop(heap)
    return -heapq.heappop(heap)



def findKth(nums : List[int], k : int) -> int:
    heapq.heapify(nums)

    for _ in range(len(nums) - k):
        heapq.heappop(nums)

    return heapq.heappop(nums)

def findKthLargest(nums : List[int], k : int) -> int :
    return heapq.nlargest(k, nums)[-1] # nsmallest

# 책 풀이4번이지만 해당 방식은 중복된 숫자가 늘어날 경우 값이 달라짐.
def findKthsort(nums : List[int], k : int) -> int :
    print(sorted(nums, reverse = True)[k-1])


topKFrequent([3,2,3,1,2,4,5,4,5,6,6], 4 )
findKthsort([3,2,3,1,2,4,5,5,4,6,6],4)