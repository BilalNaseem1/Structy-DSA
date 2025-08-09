from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def level_averages(root):
    if root is None:
        return None
    
    level = 0
    queue = deque([(root, level)])

    values = []

    while queue:
        current, level = queue.popleft()

        if len(values) == level:
            values.append([current.val])
        else:
            values[level].append(current.val)

        if current.left is not None:
            queue.append((current.left, level+1))
        
        if current.right is not None:
            queue.append((current.right, level+1))

    x = []
    for i in range(len(values)):
        x.append(sum(values[i])/len(values[i]))
    
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
