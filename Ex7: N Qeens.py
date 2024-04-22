def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False
        # Check diagonals
        if abs(board[i] - col) == row - i:
            return False
    return True

def solve_n_queens_util(n, row, board, solutions):
    if row == n:
        # If all queens are placed, add the solution to the result
        solutions.append(list(board))
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens_util(n, row + 1, board, solutions)

def solve_n_queens(n):
    solutions = []
    board = [-1] * n
    solve_n_queens_util(n, 0, board, solutions)
    return solutions

# Example usage
n = 4  # Size of the chessboard
solutions = solve_n_queens(n)
for solution in solutions:
    print(solution)