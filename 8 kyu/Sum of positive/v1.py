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
test = [1, 5, -2, -6, 10]
test2 = [1, 5, -2, -6, 10, 15, -22, 30]
test3 = [-2, -3, -4, -5, 1]

print(positive_sum(test)) # 16
print(positive_sum(test2)) # 61
print(positive_sum(test3)) # 1