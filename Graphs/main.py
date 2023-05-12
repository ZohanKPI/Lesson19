import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def find_shortest_distance(graph, source, target):

    shortest_path = nx.shortest_path(graph, source, target, weight='weight')

    overall_distance = nx.shortest_path_length(graph, source, target, weight='weight')

    return shortest_path, overall_distance

data = pd.read_csv('C:/Users/User/Desktop/GitProjects/cities.csv', header=None, delimiter=';', encoding='latin-1')

data_list = data.values.tolist()

G = nx.Graph()

for index, row in data.iterrows():
    source = row[0]
    target = row[1]
    distance = row[2]

    G.add_edge(source, target, weight=distance)

pos = nx.spring_layout(G)
nx.draw_networkx(G, pos=pos, with_labels=True)

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels)

plt.title('City Graph')

plt.show()

source_city = 'Uzhhorod'
target_city = 'Odesa'

shortest_path, overall_distance = find_shortest_distance(G, source_city, target_city)
print(f"Shortest path from {source_city} to {target_city}:")
print(shortest_path)
print("Overall distance:", overall_distance)
