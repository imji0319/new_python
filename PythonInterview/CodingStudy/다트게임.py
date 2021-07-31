def solution(dartResult):
    answer = 0
    num = ''
    s = []
    for i in range(len(dartResult)):
        # print(s)
        if '10' in s[-1:] and dartResult[i].isdigit():
            continue
        if dartResult[i:i + 2].isdigit():
            s.append(dartResult[i:i + 2])
        else:
            s.append(dartResult[i])

    nums = []
    for i in s:
        if i.isdigit():
            nums.append(int(i))
        elif i == 'S':
            nums[-1] = nums[-1] ** 1
        elif i == 'D':
            nums[-1] = nums[-1] ** 2
        elif i == 'T':
            nums[-1] = nums[-1] ** 3
        elif i == '#':
            nums[-1] = -nums[-1]
        elif i == '*':
            if len(nums) == 1:
                nums[0] = nums[0] * 2
            else:
                for i in range(len(nums) - 2, len(nums)):
                    nums[i] = nums[i] * 2



    return sum(nums)