def solution(price, money, count):
    answer = -1
    to = 0
    for i in range(count):
        to += price * (i + 1)

    if to < money:
        answer = 0
    else:
        answer = to - money

    return answer