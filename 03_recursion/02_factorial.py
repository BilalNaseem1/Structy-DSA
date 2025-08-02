def factorial(n):

    if n ==0 or n ==1:
        return 1
    
    return n * factorial(n-1)



print(factorial(3)) # -> 6
print(factorial(18)) # -> 6402373705728000
