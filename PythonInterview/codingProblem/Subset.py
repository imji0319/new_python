
# 모든 부분 집합을 리턴하라

from typing import List

def subset(nums = List[int]) -> List[List[int]] :
    result = []
    def dfs(index, path):
        print(index, path)
        # 매번 결과 추가
        result.append(path)

        for i in range(index, len(nums)):
            dfs(i+1, path +[nums[i]])

    dfs(0, [])

    return result


print(subset([1,2,3]))