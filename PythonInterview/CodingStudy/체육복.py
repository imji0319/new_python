def solution(n, lost, reserve):
    # answer = 0
    sets = set()

    # 전체 학생 번호 리스트
    for i in range(1, n + 1):
        sets.add(i)

    # 도난당한 번호 제외
    for j in lost:
        sets.remove(j)

    # 여유분 가능 번호
    re_set = set()

    #print('sets', sets)

    # 여유분 학생 먼저 제외
    for k in reserve[:]:
        if k not in sets:
            sets.add(k)
            reserve.remove(k)


    for k in reserve:
        # print(k, k-1, k+1)

        if k not in sets:
            re_set.add(k)

        else:
            if k - 1 not in sets and k - 1 not in re_set and k - 1 != 0:
                re_set.add(k - 1)

            elif k + 1 not in sets and k + 1 not in re_set and k + 1 <= n:
                re_set.add(k + 1)

    print('reverse_set', re_set)
    result = len(sets) + len(re_set)

    return result