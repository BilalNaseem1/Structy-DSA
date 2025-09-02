from collections import deque

def to_graph(edges):
    graph = {}

    for a, b in edges:

        if a not in graph:
            graph[a] = []

        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


def shortest_path(edges, node_A, node_B):
    graph = to_graph(edges)

    queue = deque( [ (node_A, 0) ] )
    visited =  set([node_A])

    while queue:
        current, distance = queue.popleft()

        if current == node_B:
            return distance
        
        for nbr in graph[current]:
            if nbr not in visited:
                visited.add(nbr)
                queue.append((nbr, distance+1))

    return -1


