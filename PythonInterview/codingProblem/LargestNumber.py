# 항목들을 조합하여 만들 수 잇는 가장 큰 수를 출력
from typing import List



class Solution:

    @staticmethod
    def to_swap(n1 : int, n2 :int ) -> bool:
        return str(n1) + str(n2) < str(n2)+str(n1)


    # 삽입정렬 구현
    def largestNumber(self, nums :List[int]) -> str:
        i = 1
        while i < len(nums):
            j = i

            while j > 0 and self.to_swap(nums[j-1] , nums[j]):
                nums[j], nums[j-1] = nums[j-1], nums[j]

                j -= 1

            i += 1

        return str(int(''.join(map(str, nums))))


s = Solution()
nums = [3, 30, 34, 5, 9]
print(s.largestNumber(nums))