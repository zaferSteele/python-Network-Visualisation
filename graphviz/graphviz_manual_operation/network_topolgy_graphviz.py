from graphviz import Digraph  # Import the Digraph class from the graphviz module

# Create a new directed graph object with a comment label
my_graph = Digraph(comment="My Network")

# Add nodes to the graph (each represents a network device/layer)
my_graph.node("core")         # Core layer
my_graph.node("distribution") # Distribution layer
my_graph.node("access1")      # First access layer device
my_graph.node("access2")      # Second access layer device

# Add edges (connections) between the nodes
my_graph.edge("core", "distribution")         # Connect core to distribution
my_graph.edge("distribution", "access1")      # Connect distribution to access1
my_graph.edge("distribution", "access2")      # Connect distribution to access2

# Print the source code of the Graphviz representation (in DOT language)
print(my_graph.source)

# Render the graph to a file (creates a .gv file and other formats like PDF or PNG if supported)
my_graph.render("output/network_topology.gv")
