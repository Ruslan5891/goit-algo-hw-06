from graph_data import G
from algorithms import dfs_iterative, bfs_iterative, path_weight
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

# ================= Візуалізація графа =================
draw_graph(G)
