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

# FUNCTIONS did by scratch for functionality_2

'''
We did by scratch the functions about centrality mesaures.
We didn't use it because that was taking too much time, so we choose 
to calculate the results using the NetworkX library.
'''

def BFS(G, s, t):
  queue = deque([s])
  visited = set()
  while queue:
    u = queue.popleft()
    if u not in visited:
      visited.add(u)
      for v in G[u]:
        queue.append(v)
        if v == t:
          return visited

  return visited

def fun_betweenness_centrality(G):
  betweenness = defaultdict(int)
  for i, s in enumerate(G):
    if i == 10:
      break
    for j, t in enumerate(G):
      if j == 10:
        break
      if s != t:
        path = BFS(G, s, t)
        for v in path:
          betweenness[v] += 1
  n = len(G)
  for v in betweenness:
    betweenness[v] /= (n-1)*(n-2)
  return betweenness

def fun_degree_centrality(G, node):
  num_neighbors = len(list(G.neighbors(node)))
  fun_degree_centrality = num_neighbors / (len(G) - 1)
  return fun_degree_centrality

def fun_pagerank_centrality(G, alpha=0.85, max_iter=100, tol=1e-6):
    n = len(G)
    pagerank = {node: 1/n for node in G}
    for i in range(max_iter):
        diff = 0
        for node in pagerank:
            rank = sum(pagerank[neighbor] / len(G[neighbor]) for neighbor in G[node])
            new_rank = (1 - alpha) / n + alpha * rank
            diff += abs(new_rank - pagerank[node])
            pagerank[node] = new_rank
        if diff < tol:
            break
    return pagerank
  

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









