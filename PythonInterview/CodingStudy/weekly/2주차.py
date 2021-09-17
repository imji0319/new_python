import numpy as np
def solution(scores):
    answer = ''
    ts = np.transpose(scores)
    ts = ts.tolist()
    for i in range(len(ts)):
        tmp = ts[i]
        ma = max(tmp)
        mi = min(tmp)

        if tmp[i] == ma and tmp.count(ma) == 1:
            tmp.remove(ma)

        elif tmp[i] == mi and tmp.count(mi) == 1:
            tmp.remove(mi)

        me = sum(tmp) / len(tmp)

        if me >= 90:
            answer += 'A'
        elif me >= 80:
            answer += 'B'
        elif me >= 70:
            answer += 'C'
        elif me >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer