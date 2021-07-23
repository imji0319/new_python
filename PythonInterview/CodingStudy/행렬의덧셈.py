def solution(arr1, arr2):
    answer = []

    for i in arr1:
        lens = len(i)
        break

    for i in range(len(arr1)):
        s = []
        for j in range(lens):
            # print(i, j)
            ss = arr1[i][j] + arr2[i][j]

            s.append(ss)

        answer.append(s)

    # print(answer)
    return answer