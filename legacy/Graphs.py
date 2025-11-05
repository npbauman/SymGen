import networkx as nx

def build_graph(ContractionDict,OperatorsDict):
    G = nx.MultiDiGraph()

    nodes = ContractionDict.get("Operators")
    for index, name in enumerate(nodes, start=1):
        G.add_node(index, name=name)

    contractions = ContractionDict.get('Oriented Contractions')
    identities = ContractionDict.get("Identities")

    for C in contractions:

        W = -1

        # Get Identities
        id1 = identities[C[0]]
        id2 = identities[C[1]]
        
        # If either index is fixed, assign a unique weight
        if OperatorsDict[nodes[id1 - 1]].get("Fixed"):
            W = 100*id1
            W += identities[:C[0]].count(identities[C[0]])
        elif OperatorsDict[nodes[id2 - 1]].get("Fixed"):
            W = 100*id2
            W += identities[:C[1]].count(identities[C[1]])

        G.add_edge(identities[C[0]], identities[C[1]], weight = W)

    # # FOR DEBUGGING
    # print(list(G.nodes.data()))
    # print(list(G.edges.data()))
    # print("")

    return G


def check_if_connected(G, OperatorsDict):

    G_test = nx.MultiDiGraph()
    G_test = G.copy()

    for node in list(G_test.nodes.data()):
        if OperatorsDict[node[1]['name']].get("Fixed"):
            G_test.remove_node(node[0])

    # FOR DEBUGGING
    # print(list(G_test.nodes.data()))

    return nx.is_connected(G_test.to_undirected())


def check_isomorphism(G1,G2):
    nm = nx.isomorphism.categorical_node_match("name", None)
    em = nx.isomorphism.numerical_multiedge_match("weight", -1)
    
    # FOR DEBUGGING
    # print(nx.is_isomorphic(G1,G2, node_match=nm, edge_match=em))
    # print(list(G1.nodes.data()))
    # print(list(G1.edges.data()))
    # print(list(G2.nodes.data()))
    # print(list(G2.edges.data()))
    # print("")

    return nx.is_isomorphic(G1,G2, node_match=nm, edge_match=em)