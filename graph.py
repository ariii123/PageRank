"""
To run the tests:
python3 graph.py

Definitions for directed and undirected graphs.

"""

import csv
import doctest


class GraphError(Exception):
    """This class is used for raising exceptions in the graph ADTs.

    >>> e = GraphError()
    >>> str(e)
    ''
    >>> f = GraphError('some message')
    >>> str(f)
    'some message'
    >>> repr(e)
    "GraphError('')"
    >>> f # interpreter does the same thing as print(repr(f))
    GraphError('some message')
    """

    def __init__(self, message=''):
        """Initialize this exception with the given message.
        The message defaults to an empty string.
        """
        super().__init__(message)
        self.message = message

    def __str__(self):
        """Return the message used to create this exception."""
        return self.message

    def __repr__(self):
        """Return the canonical string representation of this graph."""
        return f'GraphError({repr(self.message)})'


class Node:
    r"""Represents a node in a graph.

    >>> n = Node('node1', weight=80, age=90)
    >>> n.identifier()
    'node1'
    >>> d = n.attributes()
    >>> d['age']
    90
    >>> d['weight']
    80
    >>> str(n)
    'Node [node1]\n    age : 90\n    weight : 80\n'
    """

    def __init__(self, identifier, **attributes):
        """Initialize this node with the given ID.
        The keyword arguments are optional node attributes.
        """
        self._identifier = identifier
        self._attributes = attributes
        self._in_degree = 0
        self._out_degree = 0
        self._in_neighbors = None
        self._out_neighbors = None
        self._flag_in = False
        self._flag_in_neig = False
        self._flag_out = False
        self._flag_out_neig = False

    def identifier(self):
        """Return the identifier of this node."""
        return self._identifier

    def attributes(self):
        """Return a copy of this node's attribute dictionary."""
        return self._attributes.copy()

    def __str__(self):
        """Return a string representation of this node.
        Produces a representation of this node and its attributes in
        sorted, increasing, lexicographic order.
        """
        sorted_attrs = sorted(self._attributes.items())
        attr_str = '\n'.join([f"    {key} : {value}" for key, value in sorted_attrs])
        return f"Node [{self._identifier}]\n{attr_str}\n"


class Edge:
    r"""Represents a directed edge in a graph.

    >>> n1, n2 = Node('node1'), Node('node2')
    >>> e = Edge(n1, n2, size=3, cost=5)
    >>> d = e.attributes()
    >>> d['cost']
    5
    >>> d['size']
    3
    >>> e.nodes() == (n1, n2)
    True
    >>> str(e)
    'Edge from node [node1] to node [node2]\n    cost : 5\n    size : 3\n'
    """

    def __init__(self, node1, node2, **attributes):
        """Initialize this edge with the Nodes node1 and node2.
        The keyword arguments are optional edge attributes.
        """
        self._nodes = (node1, node2)
        self._attributes = attributes

    def attributes(self):
        """Return a copy of this edge's attribute dictionary."""
        return self._attributes.copy()

    def nodes(self):
        """Return a tuple of the Nodes corresponding to this edge.
        The nodes are in the same order as passed to the constructor.
        """
        return self._nodes

    def __str__(self):
        """Return a string representation of this edge.
        Produces a representation of this edge and its attributes in
        sorted, increasing, lexicographic order.
        """
        node1_id = self._nodes[0].identifier()
        node2_id = self._nodes[1].identifier()
        sorted_attrs = sorted(self._attributes.items())
        attr_str = '\n'.join([f"    {key} : {value}" for key, value in sorted_attrs])
        return f"Edge from node [{node1_id}] to node [{node2_id}]\n{attr_str}\n"


class BaseGraph:
    r"""A graph where the nodes and edges have optional attributes.
    This class should not be instantiated directly by a user.

    >>> g = BaseGraph()
    >>> len(g)
    0
    >>> g.add_node(1, a=1, b=2)
    >>> g.add_node(3, f=6, e=5)
    >>> g.add_node(2, c=3)
    >>> g.add_edge(1, 2, g=7)
    >>> g.add_edge(3, 2, h=8)
    >>> len(g)
    3
    >>> str(g.node(2))
    'Node [2]\n    c : 3\n'
    >>> g.node(4)
    Traceback (most recent call last):
        ...
    GraphError: ...
    >>> str(g.edge(1, 2))
    'Edge from node [1] to node [2]\n    g : 7\n'
    >>> g.edge(1, 3)
    Traceback (most recent call last):
        ...
    GraphError: ...
    >>> len(g.nodes())
    3
    >>> g.nodes()[0].identifier()
    1
    >>> len(g.edges())
    2
    >>> str(g.edges()[1])
    'Edge from node [3] to node [2]\n    h : 8\n'
    >>> 1 in g, 4 in g
    (True, False)
    >>> (1, 2) in g, (2, 3) in g
    (True, False)
    >>> g[1].identifier()
    1
    >>> g[(1, 2)].nodes()[0].identifier()
    1
    >>> print(g)
    BaseGraph:
    Node [1]
        a : 1
        b : 2
    Node [2]
        c : 3
    Node [3]
        e : 5
        f : 6
    Edge from node [1] to node [2]
        g : 7
    Edge from node [3] to node [2]
        h : 8
    <BLANKLINE>
    """

    def __init__(self):
        """Initialize this graph object."""
        self._nodes = {}
        self._edges = {}

    def __len__(self):
        """Return the number of nodes in the graph."""
        return len(self._nodes)

    def add_node(self, node_id, **attributes):
        """Add a node to this graph."""
        if node_id in self._nodes:
            raise GraphError(f"Node {node_id} already exists in the graph.")
        self._nodes[node_id] = Node(node_id, **attributes)

    def node(self, node_id):
        """Return the Node object for the node whose ID is node_id."""
        if node_id not in self._nodes:
            raise GraphError(f"Node {node_id} not found in the graph.")
        return self._nodes[node_id]

    def nodes(self):
        """Return a list of all the Nodes objects in this graph."""
        return sorted(self._nodes.values(), key=lambda node: node.identifier())
    
    def nodes_id(self):
        """Return a list of all the Nodes ids in this graph."""
        return sorted(self._nodes.keys())

    def add_edge(self, node1_id, node2_id, **attributes):
        """Add an edge between the nodes with the given IDs."""
        #if node1_id == node2_id:
         #   raise GraphError("Cannot add an edge from a node to itself.")
        if (node1_id, node2_id) in self._edges:
            raise GraphError(f"Edge between nodes {node1_id} and {node2_id} already exists in the graph.")
        if node1_id not in self._nodes or node2_id not in self._nodes:
            raise GraphError("Nodes for the edge not found in the graph.")
        self._edges[(node1_id, node2_id)] = Edge(self.node(node1_id), self.node(node2_id), **attributes)
        node1 = self._nodes[node1_id]
        node2 = self._nodes[node2_id]
        node1._flag_out = False
        node1._flag_out_neig = False
        node2._flag_in = False
        node2._flag_in_neig = False

    def edge(self, node1_id, node2_id):
        """Return the Edge object for the edge between the given nodes."""
        if (node1_id, node2_id) not in self._edges:
            raise GraphError(f"Edge between nodes {node1_id} and {node2_id} not found in the graph.")
        return self._edges[(node1_id, node2_id)]

    def edges(self):
        """Return a list of all the edges in this graph."""
        return sorted(self._edges.values(), key=lambda edge: (edge.nodes()[0].identifier(), edge.nodes()[1].identifier()))

    def __getitem__(self, key):
        """Return the Node or Edge corresponding to the given key."""
        if isinstance(key, tuple):
            return self.edge(*key)
        return self.node(key)

    def __contains__(self, item):
        """Return whether the given node or edge is in the graph."""
        if isinstance(item, tuple):
            return item in self._edges
        return item in self._nodes

    def __str__(self):
        """Return a string representation of the graph."""
        result = f'{type(self).__name__}:\n'
        for node in self.nodes():
            result += str(node)
        for edge in self.edges():
            result += str(edge)
        return result


class UndirectedGraph(BaseGraph):
    """An undirected graph where nodes/edges have optional attributes.

    >>> g = UndirectedGraph()
    >>> g.add_node(1, a=1)
    >>> g.add_node(2, b=2)
    >>> g.add_edge(1, 2, c=3)
    >>> len(g)
    2
    >>> g.degree(1)
    1
    >>> g.degree(2)
    1
    >>> g.edge(1, 2).nodes() == (g.node(1), g.node(2))
    True
    >>> g.edge(2, 1).nodes() == (g.node(2), g.node(1))
    True
    >>> 1 in g, 4 in g
    (True, False)
    >>> (1, 2) in g, (2, 1) in g
    (True, True)
    >>> (2, 3) in g
    False
    >>> g[1].identifier()
    1
    >>> g[(1, 2)].nodes()[0].identifier()
    1
    >>> g.add_edge(1, 1, d=4)
    Traceback (most recent call last):
        ...
    GraphError: ...
    >>> print(g)
    UndirectedGraph:
    Node [1]
        a : 1
    Node [2]
        b : 2
    Edge from node [1] to node [2]
        c : 3
    Edge from node [2] to node [1]
        c : 3
    <BLANKLINE>
    """

    def __init__(self):
        """Initialize this UndirectedGraph object."""
        super().__init__()

    def add_edge(self, node1_id, node2_id, **attributes):
        """Add an undirected edge between the nodes with the given IDs."""
        if node1_id == node2_id:
            raise GraphError("Cannot add a self-loop in an undirected graph.")
        super().add_edge(node1_id, node2_id, **attributes)
        super().add_edge(node2_id, node1_id, **attributes)

    def degree(self, node_id):
        """Return the degree of the node with the given ID."""
        if node_id not in self._nodes:
            raise GraphError(f"Node {node_id} not found in the graph.")
        degree_count = 0

        for edge_nodes in self._edges.keys():
            if node_id in edge_nodes:
                degree_count += 1
        return int(degree_count/2)


class DirectedGraph(BaseGraph):
    """A directed graph where nodes/edges have optional attributes.

    >>> g = DirectedGraph()
    >>> g.add_node(1, a=1)
    >>> g.add_node(2, b=2)
    >>> g.add_edge(1, 2, c=3)
    >>> g.in_neighbors(2)
    [1]
    >>> len(g)
    2
    >>> g.in_degree(1), g.out_degree(1)
    (0, 1)
    >>> g.in_degree(2), g.out_degree(2)
    (1, 0)
    >>> g.edge(1, 2).nodes() == (g.node(1), g.node(2))
    True
    >>> g.edge(2, 1)
    Traceback (most recent call last):
        ...
    GraphError: ...
    >>> 1 in g, 4 in g
    (True, False)
    >>> (1, 2) in g, (2, 1) in g
    (True, False)
    >>> g[1].identifier()
    1
    >>> g[(1, 2)].nodes()[0].identifier()
    1
    >>> g.add_edge(1, 1, d=4)
    >>> g.in_degree(1), g.out_degree(1)
    (1, 2)
    >>> g.in_degree(-1)
    Traceback (most recent call last):
        ...
    GraphError: ...
    >>> g.out_degree(-1)
    Traceback (most recent call last):
        ...
    GraphError: ...
    >>> print(g)
    DirectedGraph:
    Node [1]
        a : 1
    Node [2]
        b : 2
    Edge from node [1] to node [1]
        d : 4
    Edge from node [1] to node [2]
        c : 3
    <BLANKLINE>
    >>> g.add_node(4)
    >>> g.add_node(5)
    >>> g.add_edge(4,5)
    >>> g.add_edge(2,5)
    >>> g.add_edge(1,5)
    >>> g.in_neighbors(5)
    [4, 2, 1]
    """

    def __init__(self):
        """Initialize this DirectedGraph object."""
        super().__init__()

    def in_degree(self, node_id):
        """Return the in-degree of the node with the given ID."""
        if node_id not in self._nodes:
            raise GraphError(f"Node {node_id} not found in the graph.")
        
        node = self._nodes[node_id]
        if node._flag_in is False:
            node._flag_in = True          
            in_degree_count = 0
            for edge_nodes in self._edges.keys():
                if node_id == edge_nodes[1]:
                    in_degree_count += 1
            node._in_degree = in_degree_count
        return in_degree_count

    def out_degree(self, node_id):
        """Return the out-degree of the node with the given ID."""
        if node_id not in self._nodes:
            raise GraphError(f"Node {node_id} not found in the graph.")
        
        node = self._nodes[node_id]
        if node._flag_out is False:
            node._flag_out = True
            out_degree_count = 0
            for edge_nodes in self._edges.keys():
                if node_id == edge_nodes[0]:
                    out_degree_count += 1
            node._out_degree = out_degree_count
        return node._out_degree
        
    
    def out_neighbors(self, node_id):
        """Return a list of out-neighbors for the node with the given ID."""
        if node_id not in self._nodes:
            raise GraphError(f"Node {node_id} not found in the graph.")
        
        node = self._nodes[node_id]
        if node._flag_out_neig is False:
            node._flag_out_neig = True
            for node in self._nodes.values():
                node._out_neighbors = []  # Initialize out-neighbors as an empty list
            for (src, dest) in self._edges.keys():
                self._nodes[src]._out_neighbors.append(dest)
        return node._out_neighbors
    
    def in_neighbors(self, node_id):
        """Return a list of in-neighbors for the node with the given ID."""
        if node_id not in self._nodes:
            raise GraphError(f"Node {node_id} not found in the graph.")
    
        node = self._nodes[node_id]
        if node._flag_in_neig is False:
            node._flag_in_neig = True
            for node in self._nodes.values():
                node._in_neighbors = []  # Initialize in-neighbors as an empty list
            for (src, dest) in self._edges.keys():
                self._nodes[dest]._in_neighbors.append(src)
        return node._in_neighbors


def read_graph_from_csv(node_file, edge_file, directed=False):
    """Read a graph from CSV node and edge files.

    Refer to the project specification for the file formats.
    """
    result = DirectedGraph() if directed else UndirectedGraph()
    for i, filename in enumerate((node_file, edge_file)):
        attr_start = i + 1
        with open(filename, 'r', encoding="utf8") as csv_data:
            reader = csv.reader(csv_data)
            header = next(reader)
            attr_names = header[attr_start:]

            for line in reader:
                identifier, attr_values = (line[:attr_start],
                                           line[attr_start:])
                attributes = {attr_names[i]: attr_values[i]
                              for i in range(len(attr_names))}
                if i == 0:
                    result.add_node(*identifier, **attributes)
                else:
                    result.add_edge(*identifier, **attributes)
    return result


def _test():
    """Run this module's doctests."""
    doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL)


if __name__ == '__main__':
    # Run the doctests
    _test()
