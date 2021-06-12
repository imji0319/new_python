def solution(lottos, win_nums):
    answer = []

    for i in win_nums:
        for j in lottos:
            if i == j:
                answer.append(j)
    for i in answer:
        lottos.remove(i)

    result = []
    ans_len = len(answer)  # 일치 개수

    pa = lottos.count(0)
    pa_len = ans_len + pa

    if pa_len == 0:
        result.append(6)
        result.append(6)

    else:
        result.append(7 - pa_len)  # 최고 순위

        if ans_len == 0:  # 맞춘 번호 없음
            ans_len = 1

        result.append(7 - ans_len)  # 최저순위

    # print(result)
    return result