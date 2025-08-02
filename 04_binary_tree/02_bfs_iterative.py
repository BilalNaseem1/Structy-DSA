from collections import deque


class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def breadth_first_values(root):
  if root is None:
    return []
  

  values = []
  queue = deque([root])
  
  while queue:
    current = queue.popleft()
    values.append(current.val)

    if current.left is not None:
      queue.append(current.left)

    if current.right is not None:
      queue.append(current.right)

  return values


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(breadth_first_values(a) )
#    -> ['a', 'b', 'c', 'd', 'e', 'f']
