import numpy as np


def solution(board, moves):
    answer = 0

    board_t = np.transpose(board)
    basket = []

    for m in moves:
        i = 0
        while True:
            if board_t[m - 1][i] != 0:

                if board_t[m - 1][i] == basket[-1:]:
                    answer += 2
                    basket.pop()
                else:
                    basket.append(board_t[m - 1][i])

                board_t[m - 1][i] = 0
                break

            if i < len(board_t) - 1:
                i += 1
            else:
                break


    return answer