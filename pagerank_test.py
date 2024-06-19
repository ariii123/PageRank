import pandas as pd
import networkx as nx
import numpy as np
import pagerank as p
import graph as grap


edge_file = 'characters-edges.csv'  
node_file = 'characters-nodes.csv'
df = pd.read_csv(edge_file)
G = nx.from_pandas_edgelist(df, source='Node_Id_1', target='Node_Id_2', create_using=nx.DiGraph())

g = grap.read_graph_from_csv(node_file,edge_file,True)
# Compute PageRank using NetworkX
nx_pagerank = nx.pagerank(G, alpha=0.85)

# Compute PageRank using your implementation
my_pagerank_values = p.pagerank(g)
p.print_ranks(my_pagerank_values)

print('Now python pageranks: ')
p.print_ranks(nx_pagerank)

# Compare results
#for node in G.nodes():
    #print(f"Node {node}: NetworkX PageRank = {nx_pagerank[node]}")
