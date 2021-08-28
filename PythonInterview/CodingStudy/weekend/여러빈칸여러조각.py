import numpy as np

# 조각 맞추기
def sP(board, sp):
    print('NEW')
    #print(sp, len(sp), len(sp[0]), len(sp[1]))
    # board : array, sp: array

    one = True
    for i in range(len(board)-len(sp)+1):
        for j in range(len(board[0])-len(sp[0])+1):
            ss = board[i:i+len(sp), j:j+len(sp[0])]
            #print(i,j,'------')
            #print(ss)

            test = True
            if np.array_equal(ss, sp):
                print(sp)
                if i + len(sp) < len(board) and j > 0 :
                    # 왼쪽
                    if board[i:i+len(sp), j-1].any() != 0 :
                        test = False
                if j + len(sp[0]) <= len(board[0]) and i + len(sp) < len(board):
                    # 아래
                    if board[i+len(sp), j:j+len(sp[0])].any() != 0:
                        test = False
                if j + len(sp[0]) < len(board[0]) and i + len(sp) < len(board):
                    # 오른쪽
                    if board[i:i+len(sp),j+len(sp[0])].any() != 0:
                        test = False

                if j + len(sp[0]) < len(board[0]) and i > 0:
                    # 위
                    if board[i - 1, j:j + len(sp[0])].any() != 0 :
                        test = False

                if test:
                    board[i:i+len(sp), j:j+len(sp[0])] = 0
                    one = False
                    break

        if one == False:
            break

    #print(board)
    return board


# 여러 조각 넣기
# 빈칸에 여러 개의 조각이 들어갈 수 있는 경우
# 단 조각이 근처에 붙어 있을 수 없음.
def sols(board, speces):
    speces = [np.array(x) for x in speces]
    board = np.array(board)

    # 1. 가장 큰 조각 부터 확인
    speces = sorted(speces, key=lambda x: x.shape, reverse=True)

    # 2. 가장 큰 조각부터 빈칸 채우기
    for i in speces:
        board = sP(board, i)


    return board


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


