

def solution(dartresult : str) -> int:
    nums = [0]
    for s in dartresult:
        if s == "S" :
            nums[-1] **= 1
            nums.append(0)
            print('s', nums)
        elif s == 'D':
            nums[-1] **= 2
            nums.append(0)
            print('D', nums)
        elif s == 'T':
            nums[-1] **= 3
            nums.append(0)
            print('T', nums)



        elif s =='*':
            # 이전 값 & 그 이전 값 모두 두 배 처리
            nums[-2] *= 2
            if len(nums) > 2:
                nums[-3] *= 2

        elif s == '#':
            nums[-2] *= -1

        else :
            nums[-1]  = nums[-1] * 10 + int(s)
            print(nums)


        #print(s, nums, nums[-1])

    return sum(nums)




print(solution('1D2S#10S'))



