from graph_data import G, cities
from algorithms import dfs_iterative, bfs_iterative, path_weight, dijkstra
from visualize import draw_graph

start_city = "Київ"
goal_city = "Запоріжжя"

# ================= DFS і BFS =================
dfs_path = dfs_iterative(G, start_city, goal_city)
bfs_path = bfs_iterative(G, start_city, goal_city)
dfs_cost = path_weight(G, dfs_path)
bfs_cost = path_weight(G, bfs_path)

# Console output with header and separators
print("\n" + "="*60)
print("      🔹 Пошук шляхів між містами України 🔹")
print("="*60)
print(f"Шлях DFS: {dfs_path} | Вага: {dfs_cost}")
print(f"Шлях BFS: {bfs_path} | Вага: {bfs_cost}")
print("="*60 + "\n")


# ================= Dijkstra =================
# Перетворюємо граф у словник для алгоритму
graph_dict = {city: {} for city in cities}
for u, v, data in G.edges(data=True):
    graph_dict[u][v] = data['weight']
    graph_dict[v][u] = data['weight']

print("\n" + "="*60)
print("      🔹 Алгоритм Дейкстри (найкоротші шляхи) 🔹")
print("="*60 + "\n")
dijkstra_distances = dijkstra(graph_dict, start_city)

# ================= Візуалізація графа =================
draw_graph(G)
