def sum_numbers_recursive(numbers):
    if len(numbers) == 0:
        return 0
    
    return numbers[0] + sum_numbers_recursive(numbers[1:])

print(sum_numbers_recursive([5, 2, 9, 10])) # -> 26
print(sum_numbers_recursive([1, -1, 1, -1, 1, -1, 1])) # -> 1
print(sum_numbers_recursive([])) # -> 0
print(sum_numbers_recursive([1000, 0, 0, 0, 0, 0, 1])) # -> 1001
