from collections import Counter

def mostFrequent(s):
    hashmap = Counter(s)

    max_char = None
    max_val = 0
    for key, val in hashmap.items():
        
        if val > max_val:
            max_char = key
            max_val = val
    
    return max_char


if __name__ == "__main__":
    print(mostFrequent("yahoooooo"))