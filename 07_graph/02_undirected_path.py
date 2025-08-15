# if there is no undirected path for 2 nodes it means the 2 nodes are not connected.

edges = [
    ('i', 'j'),
    ('k', 'i'),
    ('m', 'k'),
    ('k', 'l'),
    ('o', 'n')
]


def build_graph(edges):
    graph = {}

    for a,b in edges:
        if a not in graph:
            graph[a] = []

        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


def has_path(graph, src, dst, visited = set()):
    if src == dst:
        return True
    
    if src in visited:
        return False
    
    visited.add(src)

    for i in graph[src]:
        if has_path(graph, i, dst) == True:
            return True

    return False


def undirected_path(edges, node_A, node_B):
    graph = build_graph(edges)

    return has_path(graph, node_A, node_B)


edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

print(undirected_path(edges, 'j', 'm')) # -> True

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

print(undirected_path(edges, 'k', 'o')) # -> False
