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

    gm = bb(game_board,0)
    ta = bb(table, 1)



    #조각이 들어오면 0,0을 기준으로 패턴의 위치를 변경하고, 회전했을 때의 가능한 모든 조각 패턴 리턴
    def rotate_shape_list(shapes):
        list = []

        # tuple -> array
        sha = np.array(shapes)

        # 패턴의 전체 크기 확인
        x = max(sha[:,0]) - min(sha[:,0]) +1
        y = max(sha[:,1]) - min(sha[:,1]) +1

        ze = np.zeros((x,y))

        # index값 변경 -> 원점 기준
        if min(sha[:,0]) > 0:
            sha[:,0] = sha[:,0] -min(sha[:,0])

        if min(sha[:,1]) > 0:
            sha[:,1] = sha[:,1] -min(sha[:,1])


        for j in sha:
            r, c = j
            ze[r,c] = 1

        list.append(ze)
        list.append(np.rot90(ze))
        list.append(np.rot90(ze,2))
        list.append(np.rot90(ze,3))



        return list


    for i in ta:
        sh_list = rotate_shape_list((i))
        for j in sh_list:
            print(j)





    return answer





print(solution([[0, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]]))

