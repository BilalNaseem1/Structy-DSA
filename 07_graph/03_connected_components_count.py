def explore(graph, node, visited):
  if node in visited:
    return False
  
  visited.add(node)

  for nbr in graph[node]:
    explore(graph, nbr, visited)

  return True


def connected_components_count(graph):
  visited = set()
  count = 0

  for i in graph:
    if explore(graph, i, visited) == True:
      count +=1

  return count
    


print(connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 2
)

