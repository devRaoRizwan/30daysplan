# Introduction
# Reversing strings (reading them from right to left, rather than from left to right) is a surprisingly common task in programming.

# For example, in bioinformatics, reversing the sequence of DNA or RNA strings is often important for various analyses, such as finding complementary strands or identifying palindromic sequences that have biological significance.

# Instructions
# Your task is to reverse a given string.

# Some examples:

# Turn "stressed" into "desserts".
# Turn "strops" into "sports".
# Turn "racecar" into "racecar".


def reverse(text):
    return text[::-1]


if __name__ == "__main__" :
    print(reverse("stressed"))