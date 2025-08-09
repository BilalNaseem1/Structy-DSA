class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def leaf_list(root):
    if root is None:
        return []
    
    values = []

    if root.right is None and root.left is None:
        return [root.val]
    
    left_values = leaf_list(root.left)
    right_values = leaf_list(root.right)

    return left_values + right_values


a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

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

print(leaf_list(a)) # -> [ 'd', 'e', 'f' ] 
