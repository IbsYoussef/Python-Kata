# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.

def disemvowel(string_):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in string_ if char not in vowels])

# Basic test cases
assert disemvowel("hello") == "hll"
assert disemvowel("world") == "wrld"
assert disemvowel("AEIOUaeiou") == ""  # All vowels should be removed

# # Mixed case
assert disemvowel("Python is Awesome!") == "Pythn s wsm!"

# # Edge cases
assert disemvowel("") == ""  # Empty string should return empty
assert disemvowel("bcdfghjklmnpqrstvwxyz") == "bcdfghjklmnpqrstvwxyz"  # No vowels, should remain the same

# # Numbers and special characters
assert disemvowel("123!@#aeiOU") == "123!@#"
assert disemvowel("H3ll0 W0rld!") == "H3ll0 W0rld!"  # Only removes vowels, keeps numbers and symbols

print("All tests passed!")
