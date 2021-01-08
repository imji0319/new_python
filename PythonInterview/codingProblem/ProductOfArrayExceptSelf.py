'''
Created on 2020. 10. 1.

@author: jihye
'''


'''
배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력 

input : List[int]
output : List[int]

* 나눗셈 금지 

'''

from typing import List


# time exceeded 
nums = [1,2,3,4]
result =[] 
for i in range(len(nums)):
    p = 1 
    list1 = nums[:i] + nums[i+1:]
    
    for j in list1:
        p = p*j

    result.append(p)

print(result)




def productExceptSelf(nums: List[int]) -> List[int]:
    
    out = []
    p = 1
    
    # 왼쪽 곱셈 
    for i in range(0, len(nums)):
        
        out.append(p)
        p = p * nums[i]
        
    p = 1 
    
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례로 곱셈 
    
    for j in range(len(nums) -1, 0-1, -1):
        out[i] = out[i] * p
        p = p * nums[i]
        
    return out
     
    




if __name__ == '__main__':
    pass