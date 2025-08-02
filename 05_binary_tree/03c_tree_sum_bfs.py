from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_sum(root):
    if root is None:
        return 0
    
    sum_ = 0
    queue = deque([root])

    while queue:
        current = queue.popleft()
        sum_ += current.val

        if current.left is not None:
            queue.append(current.left)
        
        if current.right is not None:
            queue.append(current.right)

    return sum_
    
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

print(tree_sum(a)) # -> 21
