# Task
# You get an array of numbers, return the sum of all positive ones

# Example
# [1, -4, 7, 12] => 1 + 7 + 12 = 20
# Note
# If there is nothing to sum, the sum is default to 0.

def positive_sum(arr):
    result = 0

    for n in arr:
        if n > 0:
            result += n
    
    return result

# Test Cases
assert positive_sum([1, 5, -2, -6, 10]) == 16
assert positive_sum([1, 5,-2, -6, 10, 15, -22, 30]) == 61
assert positive_sum([-2, -3, -4, -5, 1]) == 1

assert positive_sum([2, 4, 6, 8, 10]) == 30
assert positive_sum([-1, -2, -3, -4, -5]) == 0
assert positive_sum([]) == 0
assert positive_sum([5]) == 5
assert positive_sum([-10]) == 0

assert positive_sum([1000000, -500000, 2000000, -1000000]) == 3000000

assert positive_sum([0, 1, 2, 3, 0, -5]) == 6
assert positive_sum([-1000, -2000, 500, -3000, 100]) == 600

print("All tests passed!")