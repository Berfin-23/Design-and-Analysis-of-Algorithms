def dijkstra(graph, source):
    # Initialize distances
    distances = {vertex: float('infinity') for vertex in graph}
    distances[source] = 0

    # Set of visited vertices
    visited = set()

    # Queue containing all vertices
    queue = list(graph)

    while queue:
        # Find vertex with minimum distance
        current_vertex = min(queue, key=lambda vertex: distances[vertex])
        queue.remove(current_vertex)

        # Add current vertex to visited set
        visited.add(current_vertex)

        # Update distances for neighboring vertices
        for neighbor, weight in graph[current_vertex].items():
            if neighbor not in visited:
                new_distance = distances[current_vertex] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

    return distances


# Sample graph
graph = {
    'A': {'B': 3, 'C': 2},
    'B': {'A': 3, 'C': 1, 'D': 4},
    'C': {'A': 2, 'B': 1, 'D': 5},
    'D': {'B': 4, 'C': 5}
}

# Source vertex
source_vertex = 'A'

# Calculate shortest distances
shortest_distances = dijkstra(graph, source_vertex)

# Print shortest distances
print("Shortest distances from source vertex", source_vertex)
for vertex, distance in shortest_distances.items():
    print("Vertex:", vertex, "- Distance:", distance)