def solution(table, languages, preference):
    answer = ''
    pref = {}
    for i in range(len(languages)):
        pref[languages[i]] = preference[i]
    # print(pref)

    dic = {}
    for i in table:
        lit = i.split()
        co = lit[0]

        wr = {}
        for j in range(len(lit[1:])):
            if lit[j + 1] in languages:
                wr[lit[j + 1]] = 5 - j
        # print(wr)
        for i, v in wr.items():
            # print(i, v, pref[i])
            wr[i] = wr[i] * pref[i]
        s = 0
        for i in wr.values():
            s += i
        dic[co] = s
    answer = sorted(dic.items(), key=lambda x: (-x[1], x[0]))[0][0]
    return answer
