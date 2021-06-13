from collections import Counter


def solution(N, stages):
    answer = []
    plp = len(stages)
    co = Counter(stages)
    # print(co)

    result = {}
    for i in range(1, N + 1):
        s = 0
        for j in range(i):
            s += co[j]

        # print(co[i], plp - s )
        try:
            result[i] = co[i] / (plp - s)
        except ZeroDivisionError:
            result[i] = 0

    # print(result)
    result = sorted(result.items(), key=(lambda x: x[1]), reverse=True)

    answer = list(dict(result).keys())
    print(answer)

    return answer