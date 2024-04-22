def floyd_warshall(cost):
    # Number of vertices in the graph
    n = len(cost)

    # Initialize the distance matrix with the given cost matrix
    dist = [[cost[i][j] for j in range(n)] for i in range(n)]

    # Apply Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Display the current cost matrix
    print("Shortest distance between any pair of vertices:")
    for row in dist:
        print(row)


# Example usage
cost_matrix = [
    [0, 5, float('inf'), 10],
    [float('inf'), 0, 3, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]

floyd_warshall(cost_matrix)