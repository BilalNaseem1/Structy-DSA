class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree_includes(root, target):
    if root is None:
        return False
    
    if root.val == target:
        return True
    
    return tree_includes(root.left, target) or tree_includes(root.right, target)


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
print(tree_includes(a, "a")) # -> True


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

print(tree_includes(a, "n")) # -> False
