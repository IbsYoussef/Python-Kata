# Introduction
# The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

# Task
# Given a year, return the century it is in.

# Examples
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20
# 2742 --> 28

import math

def century(year):
    return math.ceil(year/100)

# Test cases
assert century(1705) == 18  # 1705 is in the 18th century
assert century(1900) == 19  # 1900 is in the 19th century
assert century(2001) == 21  # 2001 is in the 21st century
assert century(89) == 1  # 89 is in the 1st century

# Edge cases
assert century(1) == 1    # Year 1 is in the 1st century
assert century(100) == 1  # Year 100 is still in the 1st century
assert century(101) == 2  # Year 101 starts the 2nd century
assert century(1999) == 20  # Last year of the 20th century
assert century(2000) == 20  # 2000 is still in the 20th century
assert century(2001) == 21  # First year of the 21st century
assert century(2100) == 21  # 2100 is the last year of the 21st century
assert century(2101) == 22  # 2101 starts the 22nd century

# Large Numbers
assert century(10000) == 100  # Year 10000 is in the 100th century
assert century(9999) == 100  # Year 9999 is in the 100th century
assert century(50000) == 500  # Year 50000 is in the 500th century

print("All tests passed!")