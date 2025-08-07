# Write a function, bottom_right_value, that takes in the root of a binary tree. The function should return the right-most value in the bottom-most level of the tree.
from collections import deque
# You may assume that the input tree is non-empty.


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def bottom_right_value(root):
    if root is None:
        return None
    
    queue = deque([root])

    while queue:
        current = queue.popleft()

        if current.left is not None:
            queue.append(current.left)
        
        if current.right is not None:
            queue.append(current.right)

    return current.val

a = Node(3)
b = Node(11)
c = Node(10)
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
#   11     10
#  / \      \
# 4   -2     1

print(bottom_right_value(a)) # -> 1


a = Node(-1)
b = Node(-6)
c = Node(-5)
d = Node(-3)
e = Node(-4)
f = Node(-13)
g = Node(-2)
h = Node(6)
i = Node(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
e.right = h
f.left = i

#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   -4   -13
#     / \    /   
#    -2  6  7 

print(bottom_right_value(a)) # -> 7
