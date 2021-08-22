import numpy as np
def sliceP(emptyboard, spece):
    answer = -1

    board = np.array(emptyboard)
    sp = np.array(spece)
    #print(sp)
    '''
    s = np.lib.stride_tricks.sliding_window_view(board, (3,3))
    for i in s:
        for j in i :
            nn = []
            for n in j:
                nn.append(n.tolist())

            if np.array_equal(nn, sp):
                print(sp)

    '''

    #print(len(board), len(board[0]), len(board[1]))

    for i in range(len(board)-len(sp)+1):
        for j in range(len(board[0])-len(sp[0])+1):
            #print('**********')
            #print([i,j])
            ss = board[i:i+len(sp),j:j+len(sp)]

            if np.array_equal(ss, sp):
                board[i:i+len(sp[0]), j:j+len(sp[0])] = 0

    print(board)




spece = [[0, 1, 0],
         [0, 1, 0],
         [1, 1, 1]]
emptyboard = [[0,0,1,0],
              [0,0,1,0],
              [1,1,1,1],
              [1,0,0,0],
              [1,0,0,0]]



print(sliceP(emptyboard, spece))
