def solution(s, n):
    answer = ''
    L_a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    s_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # print(len(L_a))
    # print(len(s_a))
    for i in s:
        if i in L_a:
            j = L_a.index(i)
            j = j - (len(L_a) - n)

            answer += L_a[j]

        elif i in s_a:
            j = s_a.index(i)
            j = j - (len(s_a) - n)

            answer += s_a[j]

        else:
            answer += i

    return answer

