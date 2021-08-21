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

    print(bb(game_board,0))
    print(bb(table, 1))


    return answer





print(solution([[0, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]]))

