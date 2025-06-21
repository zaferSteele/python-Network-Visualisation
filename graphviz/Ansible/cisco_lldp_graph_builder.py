#!/usr/bin/env python3

# Import necessary modules
import glob, re
from graphviz import Digraph, Source

# Compile a regex pattern to match GigabitEthernet interfaces Gi0/1 to Gi0/4
pattern = re.compile('Gi0/[1234]')

# List to store LLDP edge relationships between devices
device_lldp_neighbors = []

# Walk through all files in the tmp/ directory
for file_name in glob.glob('tmp/*'):
    # Extract device name from filename, e.g., r1_lldp_output.txt → r1
    device = file_name.split('/')[1].split('_')[0]
    print("device: " + device)
    
    # Open the file and read each line
    with open(file_name, 'r') as f:
        for line in f.readlines():
            line = eval(line)  # Evaluate the line as a Python object (assumes list format)
            for item in line[0]:
                # Match only specific GigabitEthernet interfaces (Gi0/1 to Gi0/4)
                if re.search(pattern, item):
                    neighbor = item.split()[0].split('.')[0]  # Extract neighbor name
                    print("  neighbors: " + neighbor)
                    device_lldp_neighbors.append((device, neighbor))  # Store device-neighbor pair

print("*" * 10)
print("Edges: " + str(device_lldp_neighbors))  # Display extracted edges

# Initialize a Graphviz Digraph
my_graph = Digraph("My_Network")
my_graph.attr(rankdir="TB")
my_graph.attr(splines="true", nodesep="0.3", ranksep="0.3", concentrate="true")

# Manually add some fixed edges (example connections)
my_graph.edge("Client", "r6-edge")
my_graph.edge("r5-tor", "Server")

# Add dynamic edges based on LLDP neighbor info
for neighbors in device_lldp_neighbors:
    node1, node2 = neighbors
    my_graph.edge(node1, node2)

# Modify the graph source to group some nodes on the same rank
source = my_graph.source
original_text = "digraph My_Network {"
new_text = 'digraph My_Network {\nnode [shape=box]\n{rank=same Client "r6-edge"}\n{rank=same r1 r2 r3}\n'
new_source = source.replace(original_text, new_text)
print(new_source)  # Print updated DOT source

# Generate the final graph from modified DOT source and render to file
new_graph = Source(new_source, engine='dot')
new_graph.render("output/lldp_graph.gv")
