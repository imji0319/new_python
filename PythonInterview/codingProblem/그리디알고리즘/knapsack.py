
# CASE 1. 가방을 쪼갤 수 있 경우
def fractional_knapsack(cargo):
    capacity = 15

    pack = []

    # 단가 계산 역순 정렬
    for c in cargo:
        pack.append(c[0] / c[1], c[0], c[1])
    pack.sort(reverse = True)

    # 단가 순 그리드 계산
    total_value = 0

    for p in pack :
        if capacity - p[2] >= 0:
            capacity -= p[2]
            total_value += p[1]

        else :
            fraction = capacity / p[2]
            total_value += p[1]*fraction
            break

    return total_value




# CASE 2.가방을 쪼갤 수 없는 경우
def zero_one_knapstack(carge):
    capacity = 15
    pack = []

    for i in range(len(carge)+1):
        pack.append([])

        for c in range(capacity + 1):
            if i == 0 or c == 0 :
                pack[i].append(0)

            elif carge[i-1][1] <= c:
                pack[i].append(
                    max(
                        carge[i-1][0] + pack[i-1][c-carge[i-1][1]],
                        pack[i-1][c]
                    )
                )

            else :
                pack[i].append(pack[i-1][c])

    return pack[-1][-1]




