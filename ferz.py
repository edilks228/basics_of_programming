def can_place(board, row, col):
    for i in range(row):
        if board[i] == col or board[i] - col == row - i or board[i] - col == i - row:
            return False
    return True


def count_queen_placements(board, row):
    if row == 8:
        return 1

    count = 0
    for col in range(8):
        if can_place(board, row, col):
            board[row] = col
            count += count_queen_placements(board, row + 1)
            board[row] = -1

    return count


board = [-1] * 8


print( count_queen_placements(board, 0))
