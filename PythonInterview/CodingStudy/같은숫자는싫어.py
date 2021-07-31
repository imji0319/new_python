def solution(arr):
    answer = [arr[0]]
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print(answer)

    for i in arr[1:]:
        if i == answer[-1]:
            continue
        else:
            answer.append(i)

    return answer