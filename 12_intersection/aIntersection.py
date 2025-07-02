# intersection
# Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in both of the two lists.

# You may assume that each input list does not contain duplicate elements.


def hashmapGenerator(lst_, label):
    hashmap = {}

    for i in lst_:
        if i not in hashmap:
            hashmap[i] = label

    return hashmap

def intersection(a, b):
    h1 = hashmapGenerator(a, 'a')
    h2 = hashmapGenerator(b, 'b')

    final_list = []
    for i in h1:
        # print(i)
        if i in h2:
            final_list.append(i)

    return final_list
if __name__ == "__main__":
    output = intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6]
    print(output)