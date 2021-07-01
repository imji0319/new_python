

from typing import List

def slidingWindow(nums : List[int], k = int) -> int:
    if not nums :
        return nums

    result = []
    for i in range(len(nums) - k+1 ):
        result.append(max(nums[i:i+3]))

    return result


from collections import deque
def qeSlidingWindow(nums : List[int], k = int) -> int :

    if not nums :
        return nums

    result = []
    window = deque()

    current_max = float('-inf')

    for i, v in enumerate(nums):

        window.append(v)

        if i < k-1:
            continue


        if current_max == float('-inf'):
            current_max = max(window)

        elif v > current_max :
            current_max = v

        result.append(current_max)

        if current_max == window.popleft():
            current_max = float('-inf')



    return result

nums = [-1,3,-1,-3,5,3,6,7]
print(qeSlidingWindow(nums, 3))


