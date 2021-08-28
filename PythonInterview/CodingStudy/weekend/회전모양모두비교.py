'''
조각이 회전할 때 채울 수 있는 경우 처리
'''
import numpy as np





# 조각 비교
def sP(board, sp):
    #print('NEW')
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
                #print(sp)
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
    return board


# 회전 조각 list 반환
def rotation(sp):
    ro_list = []
    ro_list.append(sp.tolist())
    ro_list.append(np.rot90(sp).tolist())
    ro_list.append(np.rot90(sp,2).tolist())
    ro_list.append(np.rot90(sp,3).tolist())

    return ro_list


def rota_list(board, spss):

    speces = [np.array(x) for x in spss]
    #print(speces)
    board = np.array(board)

    speces = sorted(speces, key = lambda x:x.shape, reverse = True)

    for i in speces:
        ro_list = rotation(i)
        #print(ro_list)
        for j in ro_list:
            board = sP(board, j)

    return board


emptyboard = [[0,0,1,0,0],
              [0,1,1,1,1],
              [0,0,1,0,0],
              [0,0,0,0,0],
              [0,1,1,0,0]]
spece = [[[0, 1, 0],
         [0, 1, 0],
         [1, 1, 1]],
         [[1],
          [1]]]



print(rota_list(emptyboard,spece))