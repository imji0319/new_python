def solution(s):
    answer = ''

    l = s.split(" ")
    # print(s)

    n = 1
    for i in l:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        n += 1
        if n <= len(l):
            answer += ' '

    return answer