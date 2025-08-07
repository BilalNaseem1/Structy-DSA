class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def sum_list(head):
    sum_ = 0
    current = head

    while current is not None:
        sum_ += current.val
        current = current.next
    
    return sum_

x = Node(38)
y = Node(4)

x.next = y

# 38 -> 4

print(sum_list(x)) # 42
