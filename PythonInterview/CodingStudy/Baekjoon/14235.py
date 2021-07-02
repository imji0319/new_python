# https://www.acmicpc.net/problem/14235
# 크리스마스 선물


child = int(input()) # 거점 & 아이들 수
gift_list = set()
for _ in range(child):
    spot = input().split()

    # 아이들에게 방문
    if len(spot) == 1 and spot[0] == "0":

        if len(gift_list) == 0:
            print(-1)

        else:
            gift = max(gift_list)
            gift_list.remove(gift)

            print(gift)

    elif len(spot) != 1:
        for i in spot:
            gift_list.add(int(i))






