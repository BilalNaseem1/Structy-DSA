from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def tree_levels(root):
    if root is None:
        return None
    
    level = 0
    queue = deque([(root, level)])

    values = []

    while queue:
        current, level = queue.popleft()

        if len(values) == level:
            values.append([current.val])
        else:
            values[level].append(current.val)

        if current.left is not None:
            queue.append((current.left, level+1))
        
        if current.right is not None:
            queue.append((current.right, level+1))

        
    
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

print(tree_levels(a)) # ->
# [
#   ['a'],
#   ['b', 'c'],
#   ['d', 'e', 'f']
# ]
