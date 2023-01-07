import pandas as pd
import networkx as nx
import numpy as np
from collections import deque
from collections import defaultdict
from collections import Counter

# FUNCTIONS USED IN functionality_1
def degree_distG(G):
    degree_G = [G.degree(n) for n in G.nodes()]
    degree_counts = Counter(degree_G)
    return degree_counts

def hubs_G1(G):
    degreeG1 = [G.degree(n) for n in G.nodes()]
    ex_nodes = [n for n in G.nodes() if G.degree(n) > np.percentile(degreeG1,95)]
    return(ex_nodes)

def hubs_G2(G):
    degreeG2 = [G.degree(n) for n in G.nodes()]
    ex_nodes = [n for n in G.nodes() if G.degree(n) > np.percentile(degreeG2,95) and G.nodes[n].get('type', '') == 'comic']
    return(ex_nodes)

def density_G(G):
    n = G.number_of_nodes()
    m = G.number_of_edges()
    return 2*m/(n*(n-1))


# FUNCTION USED IN functionality_3
def shortest_path_two_nodes(node_1, node_2, G, list_nodes):
    '''
    Input = node_1 and node_2 (two heros), a graph G and a list of hero nodes list_nodes
    Output = shortest path between node_1 and node_2 without going through nodes in list nodes different from node_1 and node_2
    
    '''
    if not nx.has_path(G,node_1,node_2):
        return []
    new_list = set(list_nodes)
    new_list.remove(node_1)
    new_list.remove(node_2)
    nodes = [i for i in G.nodes if i not in new_list]
    return list(nx.shortest_path(G.subgraph(nodes), source=node_1, target=node_2, weight=None))

# FUNCTION USED IN functionality_4

def search_shortest_weighted_path(G, source, target):
    ''' 
    This function computes shortest weighted paths in the graph G between the source, 
    the starting node for path, and the target, the ending node for path, using Dijkstra's algorithm.
    It returns 0 if there is no path between the two nodes, the path otherwise.
    '''
    try:
        return nx.shortest_path(G, source, target, weight='weight', method='dijkstra')
    except: 
        return 0









