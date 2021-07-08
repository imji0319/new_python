## https://www.acmicpc.net/problem/3273

nums = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

target = int(input())
length = len(num_list)
left = 0
right = 1

n = 0

while left < right and right < length:
    sums = num_list[left] + num_list[right]
    print(num_list[left], num_list[right], sums )

    if sums == target:
        n += 1
        left += 1
        right = left+1
    elif sums < target :
        right += 1

    elif sums > target :
        left += 1
        right = left+1


print(n)








