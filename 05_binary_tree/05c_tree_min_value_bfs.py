from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def tree_min_value(root):
    if root is None:
        return None
    
    queue = deque([root])
    min_val = float('inf')
    while queue:
        current = queue.popleft()
        if current.val < min_val:
            min_val = current.val

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)
    return min_val



a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(14)
f = Node(12)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       5
#    /    \
#   11     3
#  / \      \
# 4   14     12

print(tree_min_value(a) ) # -> 3
