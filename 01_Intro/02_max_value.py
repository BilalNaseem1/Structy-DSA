def max_value(lst):
    max_val = float('-inf')

    for i in lst:
        if i > max_val:
            max_val = i


    return max_val



print(max_value([4, 7, 2, 8, 10, 9]))