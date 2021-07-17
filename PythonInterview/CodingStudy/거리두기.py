def solution(places):
    answer = [1, 1, 1, 1, 1]
    pl = []
    for i in range(5):
        pl_list = []
        for j in places[i]:
            s = []
            for n in j:
                s.append(n)
            # print(s)

            pl_list.append(s)

        pl.append(pl_list)
    # print(pl)
    for n in range(len(pl)):
        place = pl[n]
        # print(place)
        for i in range(5):
            # print(i, place[i])
            for j in range(5):
                if place[i][j] == 'P':
                    if i + 1 < 5:
                        if place[i + 1][j] == 'P':
                            answer[n] = 0
                    if j + 1 < 5:
                        if place[i][j + 1] == 'P':
                            answer[n] = 0

                    # 오른쪽 아래 대각선에 존재할 때, 거리에 빈 테이블이 있는 경우
                    if i + 1 < 5 and j + 1 < 5:
                        if (place[i + 1][j + 1] == 'P') and (place[i + 1][j] == 'O' or place[i][j + 1] == 'O'):
                            answer[n] = 0

                    # 오른쪽 위 대각선에 존재할 때, 거리에 빈 테이블이 있는 경우
                    if i - 1 > -1 and j + 1 < 5:
                        if place[i - 1][j + 1] == 'P':
                            if (place[i - 1][j] == 'O' or place[i][j + 1] == 'O'):
                                answer[n] = 0

                    # 왼쪽 아래 대각선
                    if i + 1 < 5 and j - 1 > -1:
                        if place[i + 1][j - 1] == 'P':
                            if (place[i][j - 1] == 'O') or (place[i + 1][j] == 'O'):
                                answer[n] = 0

                    # 왼쪽 위 대각선
                    if i - 1 > -1 and j - 1 > -1:
                        if place[i - 1][j - 1] == 'P':
                            if place[i][j - 1] == 'O' or place[i - 1][j] == 'O':
                                answer[n] = 0

                    # 가로 세로 두칸씩
                    if i + 2 < 5:
                        if place[i + 2][j] == 'P' and place[i + 1][j] == 'O':
                            answer[n] = 0

                    if j + 2 < 5:
                        if place[i][j + 2] == 'P' and place[i][j + 1] == 'O':
                            answer[n] = 0

    return answer