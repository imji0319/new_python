'''
세 개의 점이 입력되었을 때 사각형이 되기 위한 다른 한점을 좌표를 구하시오
입력 : [[1,4],[3,4],[3,10]]
출력 : [1,10]
'''

import collections
def solution(v):
    answer = []
    x = []
    y = []
    for i in v :
        x.append(i[0])
        y.append(i[1])

    x = collections.Counter(x)
    y = collections.Counter(y)

    for i in x:
        if x[i] < 2:
            answer.append(i)
    for i in y:
        if y[i] < 2:
            answer.append(i)

    print(answer)


solution([[1,4],[3,4],[3,10]])
solution([[1,2],[1,10],[5,2]])