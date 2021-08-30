import numpy as np
def solution(game_board, table):
    answer = -1
    # game_board 의 빈칸 조각 = 0 // table의 조작 = 1

    # 조각 인덱스
    def dfs(board, x, y, n, tmp, visited = []):

        # 범위 초과
        if x < 0 or y < 0 or x > len(board)-1 or y > len(board)-1:
            return

        # 이미 방문 완료
        if [x, y] in visited :
            return

        visited.append([x,y])

        if board[x][y] == n :
            tmp.append([x,y])
            dfs(board, x-1,y, n, tmp, visited)
            dfs(board, x+1,y, n, tmp, visited)
            dfs(board, x, y-1, n, tmp, visited)
            dfs(board, x, y+1, n, tmp, visited)

        else:
            return

        return tmp




    def bb(board, n):
        leng = len(board)
        jos = []
        visited =[]
        for i in range(leng):
            for j in range(leng):
                tmp = []

                if board[i][j] == n:
                    li = dfs(board,i,j,n,tmp,visited)
                    if li is not None :
                        jos.append(li)

        return jos
    #print(game_board)
    for i in range(len(game_board)):
        for j in range(len(game_board[1])):
            if game_board[i][j] == 0 :
                game_board[i][j] = 1
            else:
                game_board[i][j] = 0

    #print(game_board)

    ta = bb(table, 1)
    #print(ta)

    # 조각 인덱스 -> 조각 배열 반환
    def sol(sp):
        sha = np.array(sp)
        x = max(sha[:,0])-min(sha[:,0])+1
        y = max(sha[:,1])-min(sha[:,1])+1

        ze = np.zeros((x,y))

        if min(sha[:,0]) > 0:
            sha[:,0] = sha[:,0]-min(sha[:,0])

        if min(sha[:,1]) > 0:
            sha[:,1] = sha[:,1]-min(sha[:,1])

        for j in sha:
            r, c = j
            ze[r,c] = 1

        return ze

    sp_list = []
    for i in ta:
        sp_list.append(sol(i).tolist())

    # 조각 비교

    def sP(board, sp):
        # print('NEW')
        # print(sp, len(sp), len(sp[0]), len(sp[1]))
        # board : array, sp: array

        one = True
        for i in range(len(board) - len(sp) + 1):
            for j in range(len(board[0]) - len(sp[0]) + 1):
                ss = board[i:i + len(sp), j:j + len(sp[0])]
                # print(i,j,'------')
                # print(ss)

                test = True
                if np.array_equal(ss, sp):
                    # print(sp)
                    if i + len(sp) < len(board) and j > 0:
                        # 왼쪽
                        if board[i:i + len(sp), j - 1].any() != 0:
                            test = False
                    if j + len(sp[0]) <= len(board[0]) and i + len(sp) < len(board):
                        # 아래
                        if board[i + len(sp), j:j + len(sp[0])].any() != 0:
                            test = False
                    if j + len(sp[0]) < len(board[0]) and i + len(sp) < len(board):
                        # 오른쪽
                        if board[i:i + len(sp), j + len(sp[0])].any() != 0:
                            test = False

                    if j + len(sp[0]) < len(board[0]) and i > 0:
                        # 위
                        if board[i - 1, j:j + len(sp[0])].any() != 0:
                            test = False

                    if test:
                        board[i:i + len(sp), j:j + len(sp[0])] = 0
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
        ro_list.append(np.rot90(sp, 2).tolist())
        ro_list.append(np.rot90(sp, 3).tolist())

        return ro_list

    def rota_list(board, spss):

        speces = [np.array(x) for x in spss]
        # print(speces)
        board = np.array(board)

        speces = sorted(speces, key=lambda x: x.shape, reverse=True)

        for i in speces:
            ro_list = rotation(i)
            # print(ro_list)
            for j in ro_list:
                board = sP(board, j)

        return board

    before = np.array(game_board)

    #print(sp_list)
    after = rota_list(game_board, sp_list)
    print(before - after)

    return answer





print(solution([[0, 0, 0],
                [1, 1, 0],
                [1, 1, 1]],

               [[1, 1, 1],
                [1, 0, 0],
                [0, 0, 0]]))

