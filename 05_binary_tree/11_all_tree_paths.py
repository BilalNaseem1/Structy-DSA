class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def all_tree_paths(root):
    if root is None:
        return []
    
    if root.left is None and root.right is None:
        return [[root.val]]
    
    paths = []
    left_values = all_tree_paths(root.left)
    for i in left_values:
        paths.append([root.val] + i)

    right_values = all_tree_paths(root.right)
    for j in right_values:
        paths.append([root.val] + j)

    return paths


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

print(all_tree_paths(a)) # ->
# [ 
#   [ 'a', 'b', 'd' ], 
#   [ 'a', 'b', 'e' ], 
#   [ 'a', 'c', 'f' ] 
# ] 

# x = []
# x.append([6] + [[7]])
# print(x)