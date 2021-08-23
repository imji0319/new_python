import numpy as np

# 조각 맞추기
def sP(board, sp):

    #print(sp, len(sp), len(sp[0]), len(sp[1]))
    # board : array, sp: array

    one = True # 조각 1번씩만 처리
    for i in range(len(board)-len(sp)+1):
        for j in range(len(board[0])-len(sp[0])+1):
            ss = board[i:i+len(sp), j:j+len(sp[0])]
            if np.array_equal(ss, sp):
                # 근접 index 전부 처리
                board[i:i+len(sp), j:j+len(sp[0])] = 0
                board[i:i+len(sp), j-1:j+len(sp[0])]=0
                board[i:i+len(sp), j:j + len(sp[0])+1]=0
                board[i:i+len(sp)+1, j:j +len(sp[0])]=0
                board[i-1:i+len(sp), j:j+len(sp[0])]=0
                one = False
                break

        if one == False:
            break

    return board


# 여러 조각 넣기
# 빈칸에 여러 개의 조각이 들어갈 수 있는 경우
# 단 조각이 근처에 붙어 있을 수 없음.
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


# 여러 빈칸을 여러 조각으로 채우기
# 가장 큰 빈칸에 가장 큰 조각부터 넣기
def FirstBigSize(emptyboard, speces):
    answer = sols(emptyboard, speces)

    return answer



emptyboard = [[1,0,0,1,0],
              [1,0,0,1,0],
              [0,1,1,1,1],
              [0,1,0,0,0],
              [0,1,0,0,0]]
spece = [[[0, 1, 0],
         [0, 1, 0],
         [1, 1, 1]],
         [[1],
          [1]],
         [[1],
          [1]]]



print(FirstBigSize(emptyboard, spece))


