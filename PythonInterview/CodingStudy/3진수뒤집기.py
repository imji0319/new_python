def solution(n):
    answer = 0

    tri = ""

    while True:
        s = n % 3
        n = n // 3
        tri += str(s)

        if n == 0:
            break

    for i, v in enumerate(tri[::-1]):
        ss = 3 ** (i) * int(v)

        answer += ss

    return answer