def isValidSudoku(board):
    row = [[] for i in range(9)]
    column = [[] for i in range(9)]
    box = [[] for i in range(9)]

    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val != ".":
                if val in row[i]:
                    return False
                if val in column[j]:
                    return False
                if val in box[(j//3)+((i//3)*3)]:
                    return False
                row[i].append(val)
                column[j].append(val)
                box[(j//3)+((i//3)*3)].append(val)
    return True

if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    for i in board:
        print(i)

    print(isValidSudoku(board))