class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def how_high(root):
    if root is None:
        return -1
    
    left_vals = how_high(root.left)
    right_vals = how_high(root.right)

    return 1+max(left_vals, right_vals)

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g

print(how_high(a)) # -> 3
