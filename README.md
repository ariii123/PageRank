# Page rank

Implements the PageRank algorithm over a DirectedGraph.

This module can be invoked at the command line to compute the
PageRanks of the nodes in a digraph represented as two files, one with
nodes and the other with edges:
```
  python3 pagerank.py <node_file> <edge_file> [<num_iterations>]
```
The node and edge files must match the format defined in the spec.

To run the doctests in the pagerank.py script, use the following command:
```
  python3 -m doctest pagerank.py
  ```

You can also pass the -v flag to get more detailed feedback from the
tests.

The code can be tested with this command on a graph of over 1000 nodes:
```
 python3 pagerank.py email-Eu-core.txt-nodes.csv email-Eu-core.txt-edges.csv 100
```

Instead, to run the doctests from command line of the 'graph.py' script:
```
python3 graph.py
```