'''
숫자 조합 candidates를 조합하여 합이 target이 되는 원소를 나열하라. 각 원소는 중복으로 나열 가능
'''

from typing import List

def combinationSum(candidates: List[int], target:int) -> List[List[int]]:
    result = []

    def dfs(csum, index, path):
        # 종료 조건
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return

        # 자신 부터 하위 원소까지 나열 재귀 호출

        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])


    return result

print(combinationSum([2,3,6,7], 7))
