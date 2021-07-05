'''
1. 이진수, K 입력
2. 최대 K만큼 0 또는 1로 바꿨을 때 이진수 문자열에서 연속된 0 또는 1의 최대 개수 리턴

ex )
solution('01001100', 2 ) -> 6
- 01001100에서 5번째와 6번째를 0으로 변경하면 01000000 이 됨으로 연속된 개수 : 6

solution('011010010', 4 ) -> 9
- 000000000

solution('111010001', 3 ) -> 7
- 111111101

solution('111',3) -> 3
- 111

'''

# 연속된 값 최대값 세기
def listCount(li):

    maxs = 0
    for i in range(len(li)):
        n = 0
        for j in range(i, len(li)):
            if li[i] == li[j]:
                n+=1
            else :
                break
        if n > maxs :
            maxs = n

    return maxs

# 모든 변경 가능 조합 중 최대값
def com(ori, nums, ind, k ):
    maxs = 0

    result = []

    def dfs(index, path):
        result.append(path)

        for i in range(index, len(ind)):
            dfs(i+1, path+[ind[i]])

    dfs(0, [])
    result = [i for i in result if len(i) <= k]

    #print(result)

    for i in result:
        oris = ori.copy()

        for j in i :
            oris[j] = str(nums)

        n = listCount(oris)

        #print(i, oris, n)
        if n > maxs :
            maxs = n

    return maxs


# 0 또는 1로 변경했을 때의 최대값
def solution(binString : str, k : int) -> int :
    #result = 0
    ori = list(binString)

    ind0 = [i for i in range(len(ori)) if ori[i] == "0"]
    ind1 = [i for i in range(len(ori)) if ori[i] == "1"]


    com0 = com(ori, 1, ind0, k)   # 0 -> 1
    com1 = com(ori, 0, ind1, k )  # 1 -> 0

    return max(com0, com1)



print(solution('01001100', 2 ))  # 01000000 : 6
print(solution('011010010', 4 )) # 000000000 : 9
print(solution('111010001', 3 )) # 111111101 : 7
print(solution('111',3))         # 111 : 3
print(solution('10100',2))       # 00000 : 5
print(solution('00011110001000101001', 5)) # 00000000000000101001 : 13
print(solution('111011101001010101', 3))   # 111111111101010101 : 10
print(solution('11100',3))  # 11111 : 5





