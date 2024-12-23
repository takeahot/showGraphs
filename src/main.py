import json
import os
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout

def read_data(directory):
    data = []
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as f:
                data.extend(json.load(f))
    return data

def plot_graph(data):
    G = nx.DiGraph()
    
    # Add nodes and edges
    for node in data:
        if 'department_id_1c' in node and 'department_name' in node:
            G.add_node(node['department_id_1c'], label=node['department_name'])
        if 'department_id_1c' in node and 'parent_department_id_1c' in node and node['parent_department_id_1c']:
            G.add_edge(node['parent_department_id_1c'], node['department_id_1c'])
    
    # Increase the distance between nodes
    pos = graphviz_layout(G, prog='dot', args='-Grankdir=TB')
    labels = nx.get_node_attributes(G, 'label')
    
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold', arrows=True)
    plt.show()

def main():
    data = read_data('/Users/anton/Documents/vs_projects/showGraphs/data')  # Use absolute path to data directory
    plot_graph(data)

if __name__ == "__main__":
    main()