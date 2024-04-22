def minimum_multiplication(num_matrices, dimensions):
    num_subproblems = [[0] * num_matrices for _ in range(num_matrices)]
    split_positions = [[0] * num_matrices for _ in range(num_matrices)]

    for diagonal in range(1, num_matrices):
        for start in range(num_matrices - diagonal):
            end = start + diagonal
            min_operations = float('inf')
            for split in range(start, end):
                current_operations = num_subproblems[start][split] + num_subproblems[split + 1][end] + dimensions[start] * dimensions[split + 1] * dimensions[end + 1]
                if current_operations < min_operations:
                    min_operations = current_operations
                    best_split = split
            num_subproblems[start][end] = min_operations
            split_positions[start][end] = best_split

    return num_subproblems, split_positions

def print_optimal_parenthesization(split_positions, start, end):
    if start == end:
        print(f"A{start}", end="")
    else:
        print("(", end="")
        print_optimal_parenthesization(split_positions, start, split_positions[start][end])
        print_optimal_parenthesization(split_positions, split_positions[start][end] + 1, end)
        print(")", end="")

# Example usage:
num_matrices = 4
dimensions = [5, 10, 3, 12, 5]

num_subproblems, split_positions = minimum_multiplication(num_matrices, dimensions)
print("Minimum number of scalar multiplications:", num_subproblems[0][num_matrices-1])
print("Optimal parenthesization:", end=" ")
print_optimal_parenthesization(split_positions, 0, num_matrices-1)