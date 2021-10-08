import numpy as np


def solution(sizes):
    answer = 0
    result = []
    tmp = []
    # size = np.transpose(sizes)
    total = set()
    for s in sizes:
        if s[0] < s[1]:
            tmp = s[0]
            s[0] = s[1]
            s[1] = tmp

        total.add(s[0])
        total.add(s[1])
    total = sorted(total, reverse=True)
    sizes = sorted(sizes, key=lambda x: [-x[0], -x[1]])

    Dbreak = True
    for i in total:
        for j in total:
            # print(i,j)
            for s in sizes:
                if s[0] <= i and s[1] <= j:
                    pass
                else:
                    Dbreak = False
                    break
            if Dbreak != False:
                result = [i, j]
            else:
                break
        if Dbreak == False:
            break

    # print(result)
    answer = int(result[0]) * int(result[1])

    return answer