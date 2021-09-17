def solution(weights, head2head):
    ppl_head = {}
    for i in range(len(weights)):
        ppl_head[i + 1] = head2head[i]

    ppl_nu = {}

    for i, v in ppl_head.items():
        L = v.count('L')
        W = v.count('W')

        pert = 0
        try:
            pert = W / (L + W)
        except ZeroDivisionError:
            pert = 0

        n = 0
        for j in range(len(v)):
            if v[j] == 'W':
                if weights[i - 1] < weights[j]:
                    n += 1
        ppl_nu[i] = [pert, n, weights[i - 1]]

    ppl_nu = sorted(ppl_nu.items(),
                    key=lambda x: (-x[1][0], -x[1][1], -x[1][2]))

    answer = list(dict(ppl_nu).keys())

    return answer