import graph
import pagerank

def run_tests():
    # Construct the graph
    g = graph.UndirectedGraph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    print(g.degree(1))


def run_tests1():
    # Construct the graph
    g = graph.UndirectedGraph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    # Print out the edges and their attributes
    for edge in g.edges():
        print(f"Edge: {edge.nodes()} - Attributes: {edge.attributes()}")

    # Test the degree method
    assert g.degree(1) == 2
    assert g.degree(2) == 2
    assert g.degree(3) == 2


def run_tests2():
    # BaseGraph tests
    g = graph.BaseGraph()
    g.add_node(1, a=1, b=2)
    g.add_node(3, f=6, e=5)
    g.add_node(2, c=3)
    g.add_edge(1, 2, g=7)
    g.add_edge(3, 2, h=8)
    assert len(g) == 3
    assert str(g.node(2)) == "Node [2]\n    c : 3\n"
    assert str(g.edge(1, 2)) == "Edge from node [1] to node [2]\n    g : 7\n"
    assert len(g.nodes()) == 3
    assert g.nodes()[0].identifier() == 1
    assert len(g.edges()) == 2
    assert str(g.edges()[1]) == "Edge from node [3] to node [2]\n    h : 8\n"
    assert 1 in g and 4 not in g
    assert (1, 2) in g and (2, 3) not in g
    assert g[1].identifier() == 1
    assert g[(1, 2)].nodes()[0].identifier() == 1

    # UndirectedGraph tests
    g = graph.UndirectedGraph()
    g.add_node(1, a=1)
    g.add_node(2, b=2)
    g.add_edge(1, 2, c=3)
    assert len(g) == 2
    assert g.degree(1) == 1
    assert g.degree(2) == 1
    assert g.edge(1, 2).nodes() == (g.node(1), g.node(2))
    assert g.edge(2, 1).nodes() == (g.node(2), g.node(1))
    assert (1, 2) in g and (2, 1) in g and (2, 3) not in g
    assert g[1].identifier() == 1
    assert g[(1, 2)].nodes()[0].identifier() == 1

    # DirectedGraph tests
    g = graph.DirectedGraph()
    g.add_node(1, a=1)
    g.add_node(2, b=2)
    g.add_edge(1, 2, c=3)
    assert len(g) == 2
    assert g.in_degree(1) == 0
    assert g.out_degree(1) == 1
    assert g.in_degree(2) == 1
    assert g.out_degree(2) == 0
    assert g.edge(1, 2).nodes() == (g.node(1), g.node(2))
    assert (1, 2) in g and (2, 1) not in g
    assert g[1].identifier() == 1
    assert g[(1, 2)].nodes()[0].identifier() == 1

    print("All tests passed successfully!")

def test_neighbors():
    # Create a directed graph
    g = graph.DirectedGraph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    # Test neighbors for node 1
    assert g.neighbors(1) == [2, 3]

    # Test neighbors for node 2
    assert g.neighbors(2) == [3]

    # Test neighbors for node 3
    assert g.neighbors(3) == [4]

    # Test neighbors for node 4
    assert g.neighbors(4) == []

    # Test neighbors for non-existent node
    try:
        g.neighbors(5)
    except graph.GraphError:
        assert True
    else:
        assert False, "Expected GraphError for non-existent node"

    print("All tests passed!")
    print(g.nodes_id())

def test_pagerank():
    g = graph.DirectedGraph()
    g.add_node(0, airport_name='DTW')
    g.add_node(1, airport_name='AMS', country='The Netherlands')
    g.add_node(2, airport_name='ORD', city='Chicago')
    g.add_edge(0, 1, flight_time_in_hours=8)
    g.add_edge(0, 2, flight_time_in_hours=1)
    g.add_edge(1, 0, airline_name='KLM')
    g.add_edge(1, 2, airline_name='KLM')

    aux = g.in_neighbors(2)
    for ele in aux:
        print(ele," ")


# Run the test
test_pagerank()

