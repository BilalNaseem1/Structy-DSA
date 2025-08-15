def connected_components_count(graph):
    n = 0

    for i in graph:
        n += len(graph[i])

    # n = (n * (n-1)) /2
    return n



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