def depth_first_print(graph, start):
    stack = [ start ]

    while stack: # equal to while len(stack) > 0
        stack.pop()
        



graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}


depth_first_print(graph, "a")