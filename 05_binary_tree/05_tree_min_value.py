class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def tree_min_value(root):
    if root is None:
        return None
    
    min_val = float('inf')
    stack = [root]

    while stack:
        current = stack.pop()
        if current.val < min_val:
            min_val = current.val

        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)

    return min_val

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
print(tree_min_value(a)) # -> -2



a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(-4)
f = Node(-13)
g = Node(-2)
h = Node(-2)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   -4   -13
#     /       \
#    -2       -2

print(tree_min_value(a)) # -> -13
