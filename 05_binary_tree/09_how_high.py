class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def how_high(root):
    if root is None:
        return -1
    
    max_height = 0
    stack = [(root, max_height)]
    
    while stack:
        current, curr_height = stack.pop()
        max_height = max(max_height, curr_height)

        if current.right is not None:
            stack.append((current.right, curr_height+1))
        if current.left is not None:
            stack.append((current.left, curr_height+1))

    return max_height

a = Node('a')
c = Node('c')

a.right = c

#      a
#       \
#        c

print(how_high(a)) # -> 1



a = Node('a')

#      a

print(how_high(a)) # -> 0



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

