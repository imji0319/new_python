def solution(s):
    answer = ''
    ss = sorted(s, key=lambda item: ord(item), reverse=True)

    for i in ss:
        answer += i

    return answer