def rembin(s):
    return s[2:]


def solution(n, arr1, arr2):
    answer = []

    arr1 = list(map(bin, arr1))
    arr2 = list(map(bin, arr2))
    arr1 = list(map(rembin, arr1))
    arr2 = list(map(rembin, arr2))

    # 자릿수 채우기
    def corbin(s):
        if len(s) < n:
            ss = n - len(s)
            s = '0' * ss + s

        return s

    arr1 = list(map(corbin, arr1))
    arr2 = list(map(corbin, arr2))

    for i in range(n):
        li = ''
        for j in range(n):
            if arr1[i][j] == '0' and arr2[i][j] == '0':
                li = li + ' '
            elif arr1[i][j] == '1' or arr2[i][j] == '1':
                li += '#'

        answer.append(li)

    return answer