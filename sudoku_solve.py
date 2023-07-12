def is_valid(board,row,col,num):
    # check on string
    for i in range(9):
        if board[row][i] == num:
            return False
    #chek on col
    for i in range(9):
        if board[i][col] == num:
            return False

    #chek on square
    start_row = (row//3)*3
    start_col = (col//3)*3
    for i in range(3):
        for j in range(3):
            if board[start_row+i][start_col+j] == num:
                return False

    return True


#find empty cell
def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i,j
    return None,None

def Solve_sudoku(board):
    row,col = find_empty_cell(board)

    if row is None:
        return True

    for number in range(1,10):
        if is_valid(board,row,col,number):
            board[row][col] = number
            if Solve_sudoku(board):
                return True
            board[row][col] = 0
    return False
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if Solve_sudoku(sudoku_board):
    # Вывод решенного судоку
    for row in sudoku_board:
        print(row)


''' sudoku X. a new condition is added: all numbers should be different on two diagonals  '''

def is_valid_X(board,row,col,num):
    # check on string
    for i in range(9):
        if board[row][i] == num:
            return False
    #chek on col
    for i in range(9):
        if board[i][col] == num:
            return False

    #chek on square
    start_row = (row//3)*3
    start_col = (col//3)*3
    for i in range(3):
        for j in range(3):
            if board[start_row+i][start_col+j] == num:
                return False

    if row == col or row + col == 8:
        for i in range(9):
            if board[i][i] == num or board[i][8-i] == num:
                return False

    return True


#find empty cell
def find_empty_cell_X(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i,j
    return None,None

def Solve_sudoku_X(board):
    row,col = find_empty_cell_X(board)

    if row is None:
        return True

    for number in range(1,10):
        if is_valid_X(board,row,col,number):
            board[row][col] = number
            if Solve_sudoku_X(board):
                return True
            board[row][col] = 0
    return False
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if Solve_sudoku_X(sudoku_board):
    # Вывод решенного судоку
    for row in sudoku_board:
        print(row)
else:
    print('this sudoku can not be solved')


''' sudoku - asterisk: Given 9 more cells, you need to write different values in these cells'''
def is_valid_asterisk(board,row,col,num):
    # check on string
    for i in range(9):
        if board[row][i] == num:
            return False
    #chek on col
    for i in range(9):
        if board[i][col] == num:
            return False

    #chek on square
    start_row = (row//3)*3
    start_col = (col//3)*3
    for i in range(3):
        for j in range(3):
            if board[start_row+i][start_col+j] == num:
                return False

    if board[1][4] == num or board[2][2] == num or board[2][6] == num or \
        board[4][1] == num or board[4][4] == num or board[4][7] or board[7][4] == num or \
        board[6][2] == num or board[6][6]: # the worst option(
        return False

    return True


#find empty cell
def find_empty_cell_asterisk(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i,j
    return None,None

def Solve_sudoku_X(board):
    row,col = find_empty_cell_asterisk(board)

    if row is None:
        return True

    for number in range(1,10):
        if is_valid_asterisk(board,row,col,number):
            board[row][col] = number
            if Solve_sudoku_X(board):
                return True
            board[row][col] = 0
    return False
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if Solve_sudoku_X(sudoku_board):
    # Вывод решенного судоку
    for row in sudoku_board:
        print(row)
else:
    print('this sudoku can not be solved')