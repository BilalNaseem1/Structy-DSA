def uncompress(s):
    nums = '0123456789'

    i = 0
    j = 0
    output = ""
    while j < len(s):
        if s[j] in nums:
            j += 1
        else:
            number = int(s[i:j])
            output += number * s[j]
            # print(i, j)
            # print(s[i:j])
            
            j +=1
            i = j
    return output


print(uncompress("2c3a1t"))


print(uncompress("3n12e2z"))