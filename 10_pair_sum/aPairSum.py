def pairSum(numbers, target_sum):

    hashmap = {}

    for key, value in enumerate(numbers):
        compliment = target_sum - value
        if compliment in hashmap:
            return key, hashmap[compliment]
        hashmap[value] = key


if __name__ == "__main__":
    output = pairSum([4, 7, 9, 2, 5, 1], 3)
    print(output)