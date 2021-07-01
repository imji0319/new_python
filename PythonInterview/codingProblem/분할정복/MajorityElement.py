
from typing import List
def majority(nums : List[int]) -> int:

    for n in nums :
        if nums.count(n) > len(nums)//2:
            return n

import collections
def majorityEle(nums : List[int]) -> int :
    counts = collections.defaultdict(int)

    for n in nums:
        if counts[n] == 0 :
            counts[n] = nums.count[num]

        if counts[n] > len(nums) // 2:
            return n


def majorityElement(nums : List[int]) -> int:
    if not nums :
        return None

    if len(nums) == 1:
        return nums[0]

    half = len(nums)//2

    a = majorityElement(nums[:half])
    b = majorityElement(nums[half:])


    return [b,a][nums.count(a) > half]


def majority(nums):
    return sorted(nums)[len(nums)//2]

