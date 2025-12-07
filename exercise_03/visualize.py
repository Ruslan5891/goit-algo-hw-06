import matplotlib.pyplot as plt
import networkx as nx


def draw_graph(G, title="Граф міст України"):
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(14, 10))
    nx.draw(G, pos, with_labels=True, node_color="skyblue",
            node_size=2000, font_size=10, font_weight="bold")
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(title)
    plt.show()
