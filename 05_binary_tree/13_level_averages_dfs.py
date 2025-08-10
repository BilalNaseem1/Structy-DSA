from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def level_averages(root):
    if root is None:
        return None
    
    hMap = {}

    stack = [(root, 0)]

    while stack:        
        current, curr_level = stack.pop()
        if curr_level not in hMap:
            hMap[curr_level] = [current.val]
        else:
            hMap[curr_level].append(current.val)

        if current.right is not None:
            stack.append((current.right, curr_level+1))

        if current.left is not None:
            stack.append((current.left, curr_level+1))
        
    
    x = []
    for i in range(len(hMap)):
        x.append(sum(hMap[i])/len(hMap[i]))
    
    return x

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

print(level_averages(a)) # -> [ 3, 7.5, 1 ] 
