'''
라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(), 튜브(T), 제이지(J), 콘(C)
2 X 2 블록 지우기
'''

from typing import List

def solution(m, n, board : List[int]) -> int :

    board = [list(x) for x in board]
    matched = True

    while matched :
        # 1) 일치여부 판별
        matched = []
        for i in range(m -1 ):
            for j in range(n -1):
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]  != "#" :
                    matched.append([i,j])
                    
        # 2) 일치한 위치 삭제 "#"
        for i, j in matched :
            board[i][j] = board[i][j+1] = board[i+1][j+1] = board[i+1][j] = "#"

        # 3) 빈공간 블럭 처리
        for _ in range(m):
            for i in range(m - 1):
                for j in range(n):
                    if board[i+1][j] == "#":
                        board[i+1][j], board[i][j] = board[i][j], "#"


    return sum(x.count("#") for x in board)




