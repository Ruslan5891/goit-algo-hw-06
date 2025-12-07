import networkx as nx
import matplotlib.pyplot as plt

cities = [
    "Київ", "Харків", "Одеса", "Дніпро", "Львів", "Запоріжжя", "Вінниця",
    "Полтава", "Чернігів", "Житомир", "Миколаїв", "Херсон",
    "Черкаси", "Івано-Франківськ", "Тернопіль"
]

G = nx.Graph()
G.add_nodes_from(cities)

edges = [
    ("Київ", "Житомир", 140),
    ("Київ", "Чернігів", 150),
    ("Київ", "Полтава", 340),
    ("Київ", "Черкаси", 190),
    ("Київ", "Вінниця", 270),
    ("Київ", "Львів", 540),
    ("Житомир", "Львів", 350),
    ("Житомир", "Вінниця", 120),
    ("Вінниця", "Одеса", 430),
    ("Одеса", "Миколаїв", 130),
    ("Миколаїв", "Херсон", 70),
    ("Полтава", "Харків", 140),
    ("Полтава", "Дніпро", 200),
    ("Дніпро", "Запоріжжя", 85),
    ("Дніпро", "Одеса", 520),
    ("Львів", "Тернопіль", 130),
    ("Тернопіль", "Івано-Франківськ", 130),
    ("Івано-Франківськ", "Львів", 140)
]

for a, b, dist in edges:
    G.add_edge(a, b, weight=dist)

pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(14, 10))
nx.draw(G, pos, with_labels=True, node_color="skyblue",
        node_size=2000, font_size=10, font_weight="bold")

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Граф міст України")
plt.show()

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

print("\n" + "+" + "-"*45 + "+")
print(f"| {'Кількість вершин (міст)':<30} | {num_nodes:>10} |")
print("+" + "-"*45 + "+")
print(f"| {'Кількість ребер (доріг)':<30} | {num_edges:>10} |")
print("+" + "-"*45 + "+")

print("\nСтупінь вершин (кількість з'єднань):")
print("+" + "-"*25 + "+" + "-"*10 + "+")
print(f"| {'Вершина (місто)':<25} | {'Ступінь':>8} |")
print("+" + "-"*25 + "+" + "-"*10 + "+")

for city, degree in G.degree():
    print(f"| {city:<25} | {degree:>8} |")

print("+" + "-"*25 + "+" + "-"*10 + "+")
