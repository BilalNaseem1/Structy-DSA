class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_node_value(head, index):
    current = head
    idx = 0

    if index ==0:
        return head

    while idx <= index:
        idx+=1
        current = current.next

        if idx ==  index:
            return current.val
        
    return False




a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

print(get_node_value(a, 2)) # 'c'
