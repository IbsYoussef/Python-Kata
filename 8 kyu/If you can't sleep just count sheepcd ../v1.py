# If you can't sleep, just count sheeps!!

# Task:
# Given a non-negative integer, 3 for example, return a string with a murmur:
# "1 sheep...2 sheep...3 sheep..."

def count_sheep(n):
    list = []
    for n in range(1, n + 1):
        list.append(f"{n} sheep...")
    
    return "".join(list)

# Test cases
assert count_sheep(1) == "1 sheep..."
assert count_sheep(2) == "1 sheep...2 sheep..."
assert count_sheep(3) == "1 sheep...2 sheep...3 sheep..."

# Edge cases
assert count_sheep(0) == ""  # No sheep, so should return an empty string
assert count_sheep(5) == "1 sheep...2 sheep...3 sheep...4 sheep...5 sheep..."  # Check a slightly larger input

# Large numbers
assert count_sheep(10) == "1 sheep...2 sheep...3 sheep...4 sheep...5 sheep...6 sheep...7 sheep...8 sheep...9 sheep...10 sheep..."

print("All tests passed!")
