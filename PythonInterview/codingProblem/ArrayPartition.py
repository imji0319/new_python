'''
Created on 2020. 10. 1.

@author: jihye
'''


'''
n개의 페어를 이용한 min(a,b) 의 합으로 만들 수 있는 가장 큰 수를 출력


input : List[int]
output : int
'''


from typing import List

nums = [1, 4, 3, 2]
nums.sort()

pair = [nums[i] for i in range(len(nums)) if i%2 ==0]

print(sum(pair))


# 오름차순 풀이 
def arrayPartition(nums : List[int]) -> int:
    
    sum1 = 0
    pair = []
    
    nums.sort()
    
    for i in nums :
        pair.append(i)
        if len(pair) == 2: 
            sum1 += min(pair)
            
            pair = []
            
    return sum1

# 짝수번째 값의 합 계산 
def arrayPartition2(nums : List[int]) -> int:
    sum1 = 0 
    nums.sort()
    
    for i, n in enumerate(nums):
        if i%2 == 0:
            sum1+=n
            
    return sum1

# Pythonic Way
def arrayPairSum(nums: List[int]) -> int :
    return sum(sorted(nums)[::2])


if __name__ == '__main__':
    pass