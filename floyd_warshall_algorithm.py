def floyd_warshall_algorithm(graph):
    num = len(graph)
    dist = [r[:] for r in graph]  
    
    def print_grid(grid, g):
        print(f"D({g}):")
        for r in grid:
            print([x if x != float('inf') else 'inf' for x in r])
        print()

    print_grid(graph, 0)

    for g in range(num):
        for i in range(num):
            for j in range(num):
                dist[i][j] = min(dist[i][j], dist[i][g] + dist[g][j])

        print_grid(dist, g+1)

graph = [
    [0, 3, 8, float('inf'), -4],
    [float('inf'), 0, float('inf'), 1, 7],
    [float('inf'), 4, 0, float('inf'), float('inf')],
    [2, float('inf'), -5, 0, float('inf')],
    [float('inf'), float('inf'), float('inf'), 6, 0]
]

floyd_warshall_algorithm(graph)

"""
output:
D(0):
[0, 3, 8, 'inf', -4]
['inf', 0, 'inf', 1, 7]
['inf', 4, 0, 'inf', 'inf']
[2, 'inf', -5, 0, 'inf']
['inf', 'inf', 'inf', 6, 0]

D(1):
[0, 3, 8, 'inf', -4]
['inf', 0, 'inf', 1, 7]
['inf', 4, 0, 'inf', 'inf']
[2, 5, -5, 0, -2]
['inf', 'inf', 'inf', 6, 0]

D(2):
[0, 3, 8, 4, -4]
['inf', 0, 'inf', 1, 7]
['inf', 4, 0, 5, 11]
[2, 5, -5, 0, -2]
['inf', 'inf', 'inf', 6, 0]

D(3):
[0, 3, 8, 4, -4]
['inf', 0, 'inf', 1, 7]
['inf', 4, 0, 5, 11]
[2, -1, -5, 0, -2]
['inf', 'inf', 'inf', 6, 0]

D(4):
[0, 3, -1, 4, -4]
[3, 0, -4, 1, -1]
[7, 4, 0, 5, 3]
[2, -1, -5, 0, -2]
[8, 5, 1, 6, 0]

D(5):
[0, 1, -3, 2, -4]
[3, 0, -4, 1, -1]
[7, 4, 0, 5, 3]
[2, -1, -5, 0, -2]
[8, 5, 1, 6, 0]

"""
