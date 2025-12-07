from collections import deque

# ================= DFS і BFS =================
def dfs_iterative(graph, start, goal):
    visited = set()
    stack = [(start, [start])]
    while stack:
        vertex, path = stack.pop()
        if vertex == goal:
            return path
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in reversed(list(graph[vertex])):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))


def bfs_iterative(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])
    while queue:
        vertex, path = queue.popleft()
        if vertex == goal:
            return path
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))


def path_weight(graph, path):
    weight = 0
    for i in range(len(path) - 1):
        weight += graph[path[i]][path[i+1]]["weight"]
    return weight


# ================= Dijkstra =================
def print_table(distances, visited):
    print("{:<15} {:<15} {:<15}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 45)
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)
        status = "Так" if vertex in visited else "Ні"
        print("{:<15} {:<15} {:<15}".format(vertex, distance, status))
    print("\n")


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        if distances[current_vertex] == float('infinity'):
            break
        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
        visited.append(current_vertex)
        unvisited.remove(current_vertex)

    # Print only final table
    print_table(distances, visited)
    return distances
