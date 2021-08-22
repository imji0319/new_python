import numpy as np

def sP(board, sp):

    #print(sp, len(sp), len(sp[0]), len(sp[1]))
    # board : array, sp: array
    for i in range(len(board)-len(sp)+1):
        for j in range(len(board[0])-len(sp[0])+1):
            ss = board[i:i+len(sp), j:j+len(sp[0])]
            if np.array_equal(ss, sp):
                #print(ss)
                board[i:i+len(sp), j:j+len(sp[0])] = 0

    return board


# 빈칸에 여러 개의 조각이 들어갈 수 있는 경우
def sols(board, speces):
    answer = -1
    speces = [np.array(x) for x in speces]
    board = np.array(board)

    # 1. 가장 큰 조각 부터 확인
    speces = sorted(speces, key=lambda x: x.shape, reverse=True)

    # 2. 가장 큰 조각부터 빈칸 채우기
    for i in speces:
        board = sP(board, i)


    return board


spece = [[[0, 1, 0],
         [0, 1, 0],
         [1, 1, 1]],
         [[1],
          [1],
          [1]]]

emptyboard = [[0,0,1,0],
              [0,0,1,0],
              [1,1,1,1],
              [1,0,0,0],
              [1,0,0,0]]



print(sols(emptyboard, spece))