'''
Created on 2020. 10. 1.

@author: jihye
'''

'''
배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.

input : List[int]
output : List[[List]]

'''


from typing import List

# 브루트 포스  -> 타임 아웃 
def threeSum(nums : List[int]) -> List[List[int]]:
    
    result =[]
    nums.sort() # 정렬 
    
    # 브루트 포스 n^3 반복 
    
    for i in range(len(nums)-2):
        
        # 중복된 값 건너뛰기 continue
        if i >0 and nums[i] == nums[i-1]:
            continue 
        
        for j in range(i+1, len(nums)-1):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            
            for k in range(j+1, len(nums)):
                if k > j+1 and nums[k] == nums[k-1]:
                    continue
                
                
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append((nums[i],nums[j],nums[k]))
               
    
    return result



# two pointer의 합 

def threeSum2(nums : List[int]) -> List[List[int]]:
    
    result = []
    nums.sort()
    
    for i in range(len(nums)-2):
        if i >0 and nums[i] == nums[i-1]:
            continue 
        
        # 간격을 좁혀가면 sum 계산
        
        left , right = i+1, len(nums)-1
        
        while left < right:
            sum3 = nums[i] + nums[left] + nums[right]
            
            if sum3 < 0 :
                left +=1
            elif sum3 > 0 :
                right -= 1
            else:
                # sum = 0 인 경우 -> 정답 및 스킵 처리
                
                result.append((nums[i], nums[left], nums[right]))
                
                while left < right and nums[left] == nums[left+1]:
                    left+=1
                while left < right and nums[right] == nums[right-1]:
                    right-=1
                     
                
                left+=1
                right -=1
                
    return result





if __name__ == '__main__':
    pass