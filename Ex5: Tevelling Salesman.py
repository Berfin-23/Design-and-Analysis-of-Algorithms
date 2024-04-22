def tsp_with_path(graph):
    num_cities = len(graph)
    # Initialize memoization table
    memo_table = [[float('inf')] * num_cities for _ in range(2**num_cities)]
    # Initialize parent table to store the previous node in the optimal path
    parent = [[-1] * num_cities for _ in range(2**num_cities)]

    # Base case: starting point to itself has distance 0
    memo_table[1][0] = 0

    # Iterate over all subsets of vertices
    for subset_mask in range(1, 2**num_cities):
        for current_city in range(num_cities):
            if subset_mask & (1 << current_city):  # If current city is in the subset represented by the mask
                for prev_city in range(num_cities):
                    if prev_city != current_city and subset_mask & (1 << prev_city):  # If prev city is also in the subset
                        if memo_table[subset_mask ^ (1 << current_city)][prev_city] + graph[prev_city][current_city] < memo_table[subset_mask][current_city]:
                            memo_table[subset_mask][current_city] = memo_table[subset_mask ^ (1 << current_city)][prev_city] + graph[prev_city][current_city]
                            parent[subset_mask][current_city] = prev_city

    # Find the last city in the optimal path
    last_city = min(range(1, num_cities), key=lambda j: memo_table[2**num_cities - 1][j] + graph[j][0])

    # Reconstruct the optimal path
    optimal_path = []
    subset_mask = 2**num_cities - 1
    while last_city != -1:
        optimal_path.append(last_city)
        subset_mask ^= (1 << last_city)
        last_city = parent[subset_mask][last_city]

    # Reverse the path to start from the starting city
    optimal_path = [0] + optimal_path[::-1]

    # Return the minimum cost and the path
    return memo_table[2**num_cities - 1][optimal_path[-1]], optimal_path

# Example usage:
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

min_cost, min_path = tsp_with_path(graph)
print("Minimum cost:", min_cost)
print("Optimal path:", min_path)