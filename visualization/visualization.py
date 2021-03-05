from parsing import get_model
from pyvis.network import Network
import pandas as pd

got_net = Network(height="100%", width="100%", bgcolor="#222222", font_color="white", directed=True)

# set the physics layout of the network
got_net.barnes_hut()  # force_atlas_2based()#
got_data = pd.read_csv("https://www.macalester.edu/~abeverid/data/stormofswords.csv")

sources = []
targets = []
weights = []

model = get_model()
for cat in model.categories:
    # Categories
    sources.append('INITIAL')
    targets.append(cat.code)
    weights.append(cat.age['40-44']['W'])

    # Diagnoses
    for diagnosis in model.graph[cat.code]:
        sources.append(cat.code)
        targets.append(diagnosis)
        diagnosisObject = model.get_diagnosis_by_code(diagnosis)
        weights.append(diagnosisObject.age['40-44']['W'])

        # Diagnoses next
        for code, prob in diagnosisObject.next_diagnoses.items():
            sources.append(diagnosisObject.code)
            targets.append(code)
            weights.append(prob)
        # sources.append(diagnosis)
        # targets.append('INITIAL')
        # weights.append(0)

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
