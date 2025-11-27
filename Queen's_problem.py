def is_safe(board, row, col, n):
    # Check same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(n):
    board = [-1] * n     # board[i] = column position of queen in row i
    solutions = []

    def backtrack(row):
        if row == n:
            # Convert board positions into printable matrix
            solution = []
            for r in range(n):
                line = ["Q" if c == board[r] else "." for c in range(n)]
                solution.append(" ".join(line))
            solutions.append(solution)
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Reset (backtrack)

    backtrack(0)
    return solutions


# Example Usage
n = int(input("Enter value of N: "))
solutions = solve_n_queens(n)

print(f"\nTotal solutions: {len(solutions)}\n")
for sol in solutions:
    for row in sol:
        print(row)
    print()
