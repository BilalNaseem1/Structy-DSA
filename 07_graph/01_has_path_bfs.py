from collections import deque

def has_path(graph, src, dst):

    queue = deque( [ src ] )

    while queue:
        current = queue.popleft()
        if current == dst:
            return True
        
        for i in graph[current]:
            queue.append(i)

    return False


graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

print(has_path(graph, 'f', 'k'))# True
