def bellman_ford_algorithm(graph, source, nodes):
    n = len(graph)
    distance = [float('inf')] * n
    distance[source] = 0
    
    for _ in range(n - 1):
        for u in range(n):
            for v in range(n):
                if graph[u][v] != float('inf'):
                    if distance[u] + graph[u][v] < distance[v]:
                        distance[v] = distance[u] + graph[u][v]

    for u in range(n):
        for v in range(n):
            if graph[u][v] != float('inf'):
                if distance[u] + graph[u][v] < distance[v]:
                    print("Graph has negative cycle")
                    return

    for i in range(n):
        if distance[i] == float('inf'):
            print(f"No path from {nodes[source]} to {nodes[i]}")
        else:
            print(f"The Shortest distance from {nodes[source]} to {nodes[i]}: {distance[i]}")


graph = [
    [0, 7, float('inf'), 6, float('inf')],
    [float('inf'), 0, -3, float('inf'), 9],
    [float('inf'), float('inf'), 0, -2, float('inf')],
    [float('inf'), 6, 5, 0, -4],
    [2, float('inf'), 7, float('inf'), 0]
]

nodes = {0: 's', 1: 'y', 2: 'x', 3: 't', 4: 'z'}
source = 0  
bellman_ford(graph, source, nodes)

"""
output:
The Shortest distance from s to s: 0
The Shortest distance from s to y: 7
The Shortest distance from s to x: 4
The Shortest distance from s to t: 2
The Shortest distance from s to z: -2

"""
