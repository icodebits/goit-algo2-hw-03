import networkx as nx
import pandas as pd

# Створюємо орієнтований граф
G = nx.DiGraph()

# Додаємо ребра з пропускною здатністю
edges = [
    ("Термінал 1", "Склад 1", 25),
    ("Термінал 1", "Склад 2", 20),
    ("Термінал 1", "Склад 3", 15),
    ("Термінал 2", "Склад 3", 15),
    ("Термінал 2", "Склад 4", 30),
    ("Термінал 2", "Склад 2", 10),
    ("Склад 1", "Магазин 1", 15),
    ("Склад 1", "Магазин 2", 10),
    ("Склад 1", "Магазин 3", 20),
    ("Склад 2", "Магазин 4", 15),
    ("Склад 2", "Магазин 5", 10),
    ("Склад 2", "Магазин 6", 25),
    ("Склад 3", "Магазин 7", 20),
    ("Склад 3", "Магазин 8", 15),
    ("Склад 3", "Магазин 9", 10),
    ("Склад 4", "Магазин 10", 20),
    ("Склад 4", "Магазин 11", 10),
    ("Склад 4", "Магазин 12", 15),
    ("Склад 4", "Магазин 13", 5),
    ("Склад 4", "Магазин 14", 10)
]

G.add_weighted_edges_from(edges, weight="capacity")

# Додаємо супер-джерело та супер-сток
G.add_node("SuperSource")
G.add_node("SuperSink")

# Зв'язки для супер-джерела
sources = ["Термінал 1", "Термінал 2"]
sinks = ["Магазин 1", "Магазин 2", "Магазин 3", "Магазин 4", "Магазин 5", "Магазин 6",
         "Магазин 7", "Магазин 8", "Магазин 9", "Магазин 10", "Магазин 11", "Магазин 12",
         "Магазин 13", "Магазин 14"]

for source in sources:
    G.add_edge("SuperSource", source, capacity=float('inf'))

for sink in sinks:
    G.add_edge(sink, "SuperSink", capacity=float('inf'))

# Виконуємо алгоритм Едмондса-Карпа
flow_value, flow_dict = nx.maximum_flow(G, "SuperSource", "SuperSink", capacity="capacity")

# Збираємо результати у таблицю
flow_results = []

for start, destinations in flow_dict.items():
    for end, flow in destinations.items():
        if flow > 0 and start in sources + ["Склад 1", "Склад 2", "Склад 3", "Склад 4"] and end in sinks:
            flow_results.append((start, end, flow))

# Створюємо DataFrame для результатів
df_flow = pd.DataFrame(flow_results, columns=["Склад / Термінал", "Магазин", "Фактичний Потік (одиниць)"])

# Відображаємо результати
print(df_flow)