class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def path_finder(root, target):
    if root.val == target:
        return root.val
    

    return path_finder