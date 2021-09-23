from collections import deque


def solution(enter, leave):
    answer = []
    deq = deque()
    leave = deque(leave)

    inp = {}
    for i in range(len(enter)):
        inp.setdefault(i + 1, [])

    for i in range(len(enter)):
        deq.append(enter[i])

        while True:
            if len(leave) > 0:
                output = leave.popleft()

            if output in deq:
                deq.remove(output)
                inp[output] = list(deq)

            else:
                leave.appendleft(output)
                break

    for k, v in inp.items():
        for i in v:
            inp[i] = inp[i] + [k]

    for k, v in inp.items():
        answer.append(len(set(v)))

    return answer