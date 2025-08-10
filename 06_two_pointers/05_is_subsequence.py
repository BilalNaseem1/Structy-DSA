def is_subsequence(s1, s2):
    i = 0
    j = 0


    while j < len(s2):
        if s1[i] == s2[j]:
            i+=1
            j +=1
        else:
            j +=1

        if i == len(s1):
            return True
        
    return False

print(is_subsequence("bde", "abcdef"))
print(is_subsequence("bda", "abcdef"))