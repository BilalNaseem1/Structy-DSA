def longest_word(s):
    words = s.split()

    max_len = float('-inf')
    max_word = ""

    for i in words:
        if len(i)>=max_len:
            max_len = len(i)
            max_word = i


    return max_word


print(longest_word("what a wonderful world"))