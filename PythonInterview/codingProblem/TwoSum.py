'''
Created on 2020. 10. 1.

@author: jihye
'''

'''
덧셈하며 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
'''

from typing import List


# 브루트 포스  : 무차별 대입 방식 
def twoSum(nums : List[int], target : int ) -> List[int]:
    
    for i in range(len(nums)):
        
        for j in range(i + 1, len(nums)):
            
            if nums[i] + nums[j] == target:
                return [i,j]
            

# in을 이용한 탐색 
def twoSum2(nums : List[int], target : int ) -> List[int] :
    
    for i, n in enumerate(nums):
        complement = target - n  # complement + n = target
        
        if complement in nums[i+1 : ]: # target-n 값이 존재 여부  
            return nums.index(n), nums[i+1:].index(complement) + (i + 1)
            


def twoSum3(nums : List[int], target : int ) -> List[int] :
    nums_map = {}
    
    # keys <-> value
    for i, num in enumerate(nums):
        
        nums_map[num] = i
    
    
    # 타겟에서 첫번째 수를 뺸 결과(target-num) 를 키로 조회
    for i, num in enumerate(nums):
        if target - num  in nums_map and i != nums_map[target-num]:
            return nums.index(num), nums_map[target-num]
        
        
        
def twoSum4(nums : List[int], target : int ) -> List[int] :
    nums_map ={}
    # 하나의 for 문으로 통합 
    
    for i, num in enumerate(nums):
        
        if target - num in nums_map:
            return [nums_map[target-num], i]
        
        nums_map[num] = i

# 투 포인트 : if left pointer + right pointer > target then right pointer moves to left, else left pointer moves to right
# 이러한 방식은 정렬된 상태이어야 하기 때문에 해당 문제를 해결하기 위해선 어려울 수 있음 
# -> 풀이 불가 
def twoSum5(nums : List[int], target : int ) -> List[int] :
    left, right = 0, len(nums) -1 # 양끝으로 지정 
    
    while not left == right :
        
        # sum < target -> left pointer moves to right
        if nums[left] + nums[right] < target:
            left+=1
            
        # sum > target -> right pointer moves to left
        elif nums[left] + nums[right] > target:
            right -=1
            
        else : 
            return left, right
    
            
    
    

def main():
    
    nums = [2,7,9,15] ; target = 9;
    print(twoSum(nums, target))

if __name__ == '__main__':
    main()