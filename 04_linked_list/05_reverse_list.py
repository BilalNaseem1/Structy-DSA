class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_list(head):
    current = head
    prev_node = None

    while current is not None:
        next_node = current.next
        current.next = prev_node
        
        prev_node = current
        current = next_node

    return prev_node
        



a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f

print(reverse_list(a).val) # f -> e -> d -> c -> b -> a
