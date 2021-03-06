import numpy as np
import networkx as nx
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import pickle

network_node_group = []
i = 0
adjacent_edges = []
with open('adj_edges.txt') as f:
    while True:
        line = f.readline()
        line = list(map(int, line.split()))
        adjacent_edges.append(line)
        i = i + 1
        if not line:
            break
j = 0
adjacent_idx = []
with open('adj_idx_edges.txt') as f:
    while True:
        line = f.readline()
        line = list(map(int, line.split()))
        adjacent_idx.append(line)
        j = j + 1
        if not line:
            break
# print(i)
color_map = ['r', 'g', 'b', 'orange', 'purple', 'yellow']
G = nx.Graph()
# for i in range(len(adjacent_edges)):
#     for node in adjacent_edges[i]:
#         print(node)
#         G = nx.Graph()
#         network_node_group.append(G.add_node(node))
# print(len(network_group))

# print(list(G.node))

network_edges_group = {}
for k in range(0, i-1):
    edges_list = []
    center = adjacent_edges[k][0]
    e = 0
    # loop from the second node to the end
    for n1 in range(1, len(adjacent_edges[k])):
        nei1 = adjacent_edges[k][n1]  # read each node
        idx1 = adjacent_idx[k][n1]  # read the index of each node
        # assign the value of center and its neigbour to the matrix
        edges_list.append([center, nei1])
        G.add_edge(center, nei1)
        e = e+1  # count neighbour number
        
        for n2 in range(n1+1, len(adjacent_edges[k])):
            nei2 = adjacent_edges[k][n2]
            idx2 = adjacent_idx[k][n2]
            # connect those whose index is contained inside the index of itself
            if idx2 in adjacent_idx[idx1]:
                e = e+1
                edges_list.append([nei1, nei2])
                G.add_edge(nei1, nei2)
                # print(G.number_of_nodes())
    
    network_edges_group[k]=edges_list   
    x = np.random.randint(5, size=1)
    # print(edges_list)
    
    nx.draw_networkx(G, node_color=color_map[x[0]], pos=nx.spring_layout(
    G, k=0.25, iterations=50), node_size=100, with_labels=True)

# print(adjacent_edges)
# print(G.number_of_nodes())
# print(G.number_of_edges())
# plt.subplot(121)
# plt.axis('off')
# plt.show()

# the label of this network is the index of lung_case
file = open('network_edges_group.pickle', 'wb')
pickle.dump(network_edges_group, file)
file.close()

