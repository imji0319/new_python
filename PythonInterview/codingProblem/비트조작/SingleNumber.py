from typing import List

def singleNumber(nums : List[int]) -> int :

    result = 0

    for i in nums :
        result ^= i
        #print(result)

    return result

#singleNumber([2,2,1])