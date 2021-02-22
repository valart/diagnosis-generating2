# import networkx as nx
# import matplotlib.pyplot as plt
from parsing import get_model
#
#
# model = get_model()
#
# G = nx.DiGraph()
# G.add_edges_from(
#     [('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E', 'F'),
#      ('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G')])
#
# val_map = {'A': 1.0,
#            'D': 0.5714285714285714,
#            'H': 0.0}
#
# values = [val_map.get(node, 0.25) for node in G.nodes()]
# print(values)
# # Specify the edges you want here
# red_edges = [('A', 'C'), ('E', 'C')]
# edge_colours = ['black' if not edge in red_edges else 'red'
#                 for edge in G.edges()]
# black_edges = [edge for edge in G.edges() if edge not in red_edges]
#
# # Need to create a layout when doing
# # separate calls to draw nodes and edges
# pos = nx.spring_layout(G)
# print(pos)
# nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),
#                        node_color = values, node_size = 200)
# nx.draw_networkx_labels(G, pos)
# nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True, width=[1, 0.5])
# nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=True)
# plt.show()

from pyvis.network import Network
import pandas as pd

got_net = Network(height="100%", width="100%", bgcolor="#222222", font_color="white", directed=True)

# set the physics layout of the network
got_net.force_atlas_2based()#barnes_hut()
got_data = pd.read_csv("https://www.macalester.edu/~abeverid/data/stormofswords.csv")

sources = []
targets = []
weights = []

model = get_model()
for cat in model.categories:
    sources.append('INITIAL')
    targets.append(cat.code)

    weights.append(cat.age['40-49']['W'])
    for diag in cat.diagnoses:
        sources.append(cat.code)
        targets.append(diag.code)
        weights.append(diag.age['40-49']['W'])

edge_data = zip(sources, targets, weights)

for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    got_net.add_node(src, src, title=src)
    got_net.add_node(dst, dst, title=dst)
    got_net.add_edge(src, dst, value=w, title=w)

neighbor_map = got_net.get_adj_list()

# add neighbor data to node hover data
for node in got_net.nodes:
    node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
    node["value"] = len(neighbor_map[node["id"]])

got_net.show("diagnosis.html")
