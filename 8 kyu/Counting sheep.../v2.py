# Instructions
# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

# For example,

# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
# The correct answer would be 17.

# Hint: Don't forget to check for bad values like null/undefined

def count_sheeps(sheeps):
    return [bool(sheep) for sheep in sheeps].count(True)

# Test Cases

# Normal case: mixed True and False
assert count_sheeps([True, False, True, True, False, True]) == 4 , "Failed, normal case"

# All True
assert count_sheeps([True, True, True,]) == 3, "Failed all True case"

# All False
assert count_sheeps([False, False, False]) == 0, "Failed all False case"

# Empty Array
assert count_sheeps([]) == 0, "Failed empty array case"

# None Values
assert count_sheeps([True, None, False, True]) == 2, "Failed None values case"

# Non-boolean values
assert count_sheeps([True, 1, 0, "sheep", False]) == 3, "Failed non-boolean values case"

print("All tests passed!")