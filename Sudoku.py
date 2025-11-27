def print_board(board):
    for i, row in enumerate(board):
        line = ""
        for j, num in enumerate(row):
            line += str(num) + " "
            if (j + 1) % 3 == 0 and j < 8:
                line += "| "
        print(line.strip())
        if (i + 1) % 3 == 0 and i < 8:
            print("- " * 11)

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def valid(board, num, pos):
    row, col = pos
    if any(board[row][i] == num for i in range(9)):
        return False
    if any(board[i][col] == num for i in range(9)):
        return False
    box_x = (col // 3) * 3
    box_y = (row // 3) * 3
    for i in range(box_y, box_y + 3):
        for j in range(box_x, box_x + 3):
            if board[i][j] == num:
                return False
    return True

def solve(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if valid(board, num, (row, col)):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0
    return False

if __name__ == "__main__":
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    print("Original:")
    print_board(puzzle)
    if solve(puzzle):
        print("\nSolved:")
        print_board(puzzle)
    else:
        print("No solution exists.")