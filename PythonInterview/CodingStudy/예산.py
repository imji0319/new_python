def solution(d, budget):
    answer = 0
    d.sort()
    s = 0
    for i in d:
        s += i
        answer += 1
        if s > budget:
            answer -= 1
            break

    return answer





d = [1,3,2,4,5]
budget = 9

print(solution(d,budget))