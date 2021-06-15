## https://www.acmicpc.net/problem/10951

import sys

while True :
    nums = sys.stdin.readline().rstrip().split()
    if nums :
        print(int(nums[0]) + int(nums[1]))
    else:
        break