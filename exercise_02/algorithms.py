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
