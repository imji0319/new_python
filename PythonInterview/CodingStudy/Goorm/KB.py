
'''
ATM기계 인출금 알고리즘
첫줄 : 거래 횟수와 현재 잔고
입금할때는 양수로 출금할때는 음수로 값이 입력된다.
만약 출금하고자하는 금액이 잔고보다 많을 경우 아무일도 일어나지 않는다.
이때 잔고를 출력하라.
'''

user_input = input().split()
curr = int(user_input[1])
for _ in range(int(user_input[0])):

    m = int(input())

    if m > 0 :
        curr+=m
    else : # 음수
        if curr - (-m) > 0:
            curr += m


print(curr)

'''
N,money = map(int,input().split())
for _ in range(N):
    m = int(input())
    If money+m>=0: money += m

print(money)
'''

