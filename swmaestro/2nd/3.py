import sys

def get_max(board):
    m = 0
    for b in board:
        for i in b:
            m = max(m, i)

    return m

def cut_board(board, x1, y1, x2, y2):
    bb = []
    for i in range(x1, x2+1):
        bb.append(board[i][y1:y2+1])
    return bb
            

result = 0

def f(board, value):
    global result
    
    N = len(board)
    M = len(board[0])

    if N == 1 and M == 1:
        result = max(result, value)
        return

    case_1 = []
    case_2 = []
    if N // 2 != 0:
        case_1.append((0, 0, N//2-1, M-1))
        case_1.append((N//2, 0, N-1, M-1))

    if M // 2 != 0:
        case_2.append((0, 0, N-1, M//2-1))
        case_2.append((0, M//2, N-1, M-1))

    if len(case_1) > 0:
        for i in range(2):
            x1, y1, x2, y2 = case_1[i]
            n_x1, n_y1, n_x2, n_y2 = case_1[(i+1)%2]

            new_board = cut_board(board, n_x1, n_y1, n_x2, n_y2)
            dev_board = cut_board(board, x1, y1, x2, y2)
            new_val = value + get_max(dev_board)

            f(new_board, new_val)

    if len(case_2) > 0:
        for i in range(2):
            x1, y1, x2, y2 = case_2[i]
            n_x1, n_y1, n_x2, n_y2 = case_2[(i+1)%2]
            new_board = cut_board(board, n_x1, n_y1, n_x2, n_y2)
            dev_board = cut_board(board, x1, y1, x2, y2)
            new_val = value + get_max(dev_board)

            f(new_board, new_val)


def main():
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    f(board, 0)
    
    # get_max(board, 0, 0, 1, 1)
    # cut_board(board, 0, 0, 1, 1)

    print(result)










if __name__=="__main__":
    main()