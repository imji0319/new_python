def finditem(li, item):
    result = [[i, j] for i, line in enumerate(li)
              for j, char in enumerate(line) if char == item]

    result = [item for i in result for item in i]

    return result


def solution(numbers, hand):
    answer = ''
    # print(numbers)
    left_nums = [1, 4, 7, "*"]
    right_nums = [3, 6, 9, "#"]
    mid_nums = [2, 5, 8, 0]

    left_hand = "*"
    right_hand = "#"

    keypad = [left_nums, mid_nums, right_nums]

    for i in numbers:
        if i in left_nums:
            answer += 'L'
            left_hand = i
        elif i in right_nums:
            answer += 'R'
            right_hand = i
        else:
            le = finditem(keypad, left_hand)
            ri = finditem(keypad, right_hand)
            mi = finditem(keypad, i)

            le_d = abs(le[0] - mi[0]) + abs(le[1] - mi[1])
            ri_d = abs(ri[0] - mi[0]) + abs(ri[1] - mi[1])

            if le_d > ri_d:
                answer += "R"
                right_hand = i
            elif le_d < ri_d:
                answer += "L"
                left_hand = i
            else:
                if hand == "left":
                    answer += "L"
                    left_hand = i
                else:
                    answer += "R"
                    right_hand = i

    return answer


