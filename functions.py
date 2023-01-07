
#FUNCTIONS USED IN functionality_3
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










