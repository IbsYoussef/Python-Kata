# Write a function that accepts a non-negative integer n and a string s as parameters, and returns a string of s repeated exactly n times.
# Examples (input -> output)
# 6, "I"     -> "IIIIII"
# 5, "Hello" -> "HelloHelloHelloHelloHello"

def repeat_str(repeat, string):
    return string * repeat

# Test Cases
assert repeat_str(3, "abc") == "abcabcabc"
assert repeat_str(2, "hello") == "hellohello"

# Edge cases
assert repeat_str(0, "test") == ""  # Should return an empty string
assert repeat_str(1, "single") == "single"  # Should return the string as is

# Large number of repetitions
assert repeat_str(5, "a") == "aaaaa"
assert repeat_str(10, "X") == "XXXXXXXXXX"

# Empty string cases
assert repeat_str(3, "") == ""  # Empty string repeated any number of times should be empty
assert repeat_str(0, "") == ""  # Edge case: 0 repetitions of an empty string

# Special characters
assert repeat_str(4, "!") == "!!!!"
assert repeat_str(2, " ") == "  "  # Space should be repeated

# Numbers as strings
assert repeat_str(3, "123") == "123123123"
assert repeat_str(2, "0") == "00"

print("All tests passed!")
