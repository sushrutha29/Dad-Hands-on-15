import heapq

def dijkstra(graph, first):
    distances = {node: float('inf') for node in graph}
    distances[first] = 0
    queue = [(0, first)]

    while queue:
        present_distance, present_node = heapq.heappop(queue)

        if present_distance > distances[present_node]:
            continue

        for Adj_Node, weight in graph[present_node].items():
            distance = present_distance + weight
            if distance < distances[Adj_Node]:
                distances[Adj_Node] = distance
                heapq.heappush(queue, (distance, Adj_Node))

    return distances


graph = {
    's': {'t': 10, 'y': 5},
    't': {'x': 1, 'z': 4},
    'x': {'z': 6},
    'y': {'t': 3, 'x': 9, 'z': 2},
    'z': {'s': 7, 'x': float('inf')}
}

startingnode = 's'
distances = dijkstra(graph, startingnode)

print("Shortest distance from", startingnode + ":")
for node, distance in distances.items():
    print(node + ":", distance)


'''
output:
Shortest distance from s:
s: 0
t: 8
x: 9
y: 5
z: 7
'''
