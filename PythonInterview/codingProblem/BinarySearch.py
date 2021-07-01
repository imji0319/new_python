nums = [-1,0,3,5,9,12]
target = 9

from typing import List
def search(nums : List[int] , target : int) -> int :
    for i in range(len(nums)):
        if nums[i] == target:
            return i



# 이진분리

def Bisearch(nums : List[int], target : int) -> int:

    def binary(left, right):
        if left <= right :
            mid = ( left + right )//2

            if nums[mid] < target:
                return binary(mid + 1, right)

            elif nums[mid] > target :
                return binary(left, mid-1)

            else :
                return mid
        else:
            return -1

    return binary(0, len(nums)-1)


# 반복풀이
def repSearch(nums : List[int], target : int ) -> int :
    left, right = 0, len(nums)-1

    while left <= right :
        mid = (left + right) // 2

        if nums[mid] < target :
            left = mid + 1
        elif nums[mid] > target :
            right = mid - 1
        else :
            return mid

    return -1


# 이진 모듈
import bisect
def MoSearch(nums : List[int], target: int) -> int:

    index = bisect.bisect_left(nums, target)

    if index < len(nums) and nums[index] == target:
        return index

    else :
        return -1



# 초간단

def searchs(nums: List[int], target : int )-> int :
    try :
        return nums.index(target)
    except:
        return -1

print(searchs(nums, target))
