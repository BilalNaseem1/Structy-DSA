def compress(s):
    i = 0
    j = 0
    output = ""
    while j< len(s):
        if s[j] == s[i]:
            j +=1

        else:
            # print(len(s[i:j]))
            if len(s[i:j]) > 1:
                output += str(len(s[i:j]))
            output += s[i]
            i = j
            j+=1

    if len(s[i:j]) > 1:
        output += str(len(s[i:j]))
    output += s[i]
    return output



print(compress('ccaaatsss'))
# print(compress('ssssbbz'))