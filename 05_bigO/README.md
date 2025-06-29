# Time Complexity Lecture

Time complexity describes how the runtime of an algorithm grows as the input size increases. It's expressed using Big O notation, which describes the upper bound of an algorithm's growth rate.

## $O(1)$ - Constant Time

Operations that take the same amount of time regardless of input size.

**Examples:**
- Arithmetic operations
- Variable assignment
- Grabbing a single index from a string or a list
- Checking a key in a dictionary
- Stack push/pop operations
- Accessing array elements by index
- Simple comparisons

```python
a = 4
b = a + 10

# grabbing index from a string
string_var = "amazing"
string_var[3]

# grabbing index from a list
lst = [3, 8, 1, 7]
lst[2]

# checking a key in a dictionary
stuff = {'a': 1, 'b': 7, 'c': 9, 'd': 0}
if 'c' in stuff:
    print("yes")

# stack operations
stack = []
stack.append(5)  # O(1)
stack.pop()      # O(1)

# simple comparisons
x = 10
y = 20
result = x > y   # O(1)
```

## $O(n)$ - Linear Time

Operations that scale linearly with input size.

**Examples:**
- Checking an item in a list
- Linear search
- Iterating through an array once
- Finding min/max in unsorted array
- Copying an array
- Simple loops that run n times

```python
# Checking an item in a list
colors = ['red', 'green', 'blue', 'orange']
print('green' in colors)  # O(n) - might check every element

# Linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Finding maximum in array
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# Copying an array
original = [1, 2, 3, 4, 5]
copy = original[:]  # O(n)

# Simple loop
def print_all(arr):
    for item in arr:  # O(n)
        print(item)
```

## $O(log n)$ - Logarithmic Time

Operations that divide the problem in half each step.

**Examples:**
- Binary search on sorted array
- Finding height of balanced binary tree
- Operations on balanced binary search trees

```python
# Binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Finding height of binary tree (recursive)
def tree_height(node):
    if not node:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))
```

## $O(n log n)$ - Linearithmic Time

Common in efficient sorting algorithms that use divide-and-conquer.

**Examples:**
- Merge sort
- Quick sort (average case)
- Heap sort
- Sorting operations in Python

```python
# Merge sort implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Python's built-in sort
arr = [64, 34, 25, 12, 22, 11, 90]
arr.sort()  # O(n log n)
```

## $O(n^2)$ - Quadratic Time

Operations with nested loops over the input.

**Examples:**
- Bubble sort
- Insertion sort
- Selection sort
- Nested loops
- Comparing all pairs

```python
# Bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Finding all pairs
def find_pairs(arr):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            pairs.append((arr[i], arr[j]))
    return pairs

# Selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Matrix multiplication (naive approach)
def matrix_multiply(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    result = [[0] * cols_B for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result
```

## $O(n^3)$ - Cubic Time

**Examples:**
- Triple nested loops
- Some dynamic programming solutions
- Matrix multiplication (standard algorithm)

```python
# Triple nested loops
def three_sum(arr):
    result = []
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    result.append([arr[i], arr[j], arr[k]])
    return result

# Floyd-Warshall algorithm for shortest paths
def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist
```

## $O(2^n)$ - Exponential Time

**Examples:**
- Recursive Fibonacci (naive)
- Subset generation
- Tower of Hanoi
- Brute force solutions

```python
# Naive Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Generate all subsets
def generate_subsets(arr):
    def backtrack(start, current):
        subsets.append(current[:])
        for i in range(start, len(arr)):
            current.append(arr[i])
            backtrack(i + 1, current)
            current.pop()
    
    subsets = []
    backtrack(0, [])
    return subsets

# Tower of Hanoi
def hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n - 1, auxiliary, destination, source)
```

## $O(n!)$ - Factorial Time

**Examples:**
- Generating all permutations
- Traveling salesman problem (brute force)
- Solving N-Queens with brute force

```python
# Generate all permutations
def permutations(arr):
    if len(arr) <= 1:
        return [arr]
    
    result = []
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for perm in permutations(rest):
            result.append([arr[i]] + perm)
    return result

# Traveling salesman (brute force)
def traveling_salesman(cities, distances):
    from itertools import permutations as perms
    min_cost = float('inf')
    best_path = None
    
    for path in perms(cities):
        cost = calculate_path_cost(path, distances)
        if cost < min_cost:
            min_cost = cost
            best_path = path
    
    return best_path, min_cost
```

## Key Rules and Guidelines

### Rule 1: Drop Constants
$O(2n) = O(n)$, $O(3n^2) = O(n^2)$

### Rule 2: Drop Lower Order Terms
$O(n^2 + n) = O(n^2)$, $O(n + log n) = O(n)$

### Rule 3: Different Inputs Use Different Variables
```python
def function(arr1, arr2):
    # This is O(a + b), not O(n)
    for item in arr1:  # O(a)
        print(item)
    for item in arr2:  # O(b)
        print(item)
```

### Rule 4: Nested Loops Usually Multiply
```python
def nested_function(arr1, arr2):
    # This is O(a * b)
    for item1 in arr1:
        for item2 in arr2:
            print(item1, item2)
```

### Rule 5: Recursive Complexity
For recursive functions: $T(n) = \text{number of recursive calls} \times \text{work per call}$

### Rule 6: Amortized Analysis
Some operations have different worst-case and average-case complexities:
- Dynamic array append: O(1) amortized, O(n) worst case
- Hash table operations: O(1) average, O(n) worst case

## Space Complexity

Don't forget about space complexity - how much extra memory an algorithm uses:

```python
# O(1) space - only using a few variables
def sum_array(arr):
    total = 0  # O(1) space
    for num in arr:
        total += num
    return total

# O(n) space - creating new array
def double_array(arr):
    result = []  # O(n) space
    for num in arr:
        result.append(num * 2)
    return result

# O(n) space - recursive call stack
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)  # O(n) call stack
```

## Common Data Structure Operations

| Data Structure | Access | Search | Insertion | Deletion |
|----------------|--------|--------|-----------|----------|
| Array          | O(1)   | O(n)   | O(n)      | O(n)     |
| Dynamic Array  | O(1)   | O(n)   | O(1)*     | O(n)     |
| Linked List    | O(n)   | O(n)   | O(1)      | O(1)     |
| Stack          | O(n)   | O(n)   | O(1)      | O(1)     |
| Queue          | O(n)   | O(n)   | O(1)      | O(1)     |
| Hash Table     | N/A    | O(1)*  | O(1)*     | O(1)*    |
| Binary Tree    | O(n)   | O(n)   | O(n)      | O(n)     |
| BST            | O(log n)* | O(log n)* | O(log n)* | O(log n)* |
| Heap           | O(1)   | O(n)   | O(log n)  | O(log n) |

*Average case; worst case may differ

## Tips for Analysis

1. **Identify the input size**: What variable represents the size of your input?
2. **Count operations**: How many times does each line execute?
3. **Focus on worst case**: What's the maximum number of operations?
4. **Consider all inputs**: Different input sizes and types
5. **Practice**: Analyze algorithms you write and encounter

Remember: Big O describes the upper bound of growth rate, helping us understand how algorithms scale with larger inputs.