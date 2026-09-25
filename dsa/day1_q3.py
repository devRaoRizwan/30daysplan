# 242. Valid Anagram
# Easy

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.


def isAnagram( s: str, t: str) -> bool:
    seen_s = {}
    seen_t = {}
    for char in s :
        if char in seen_s :
            seen_s[char] += 1
        else :
            seen_s[char] = 1

    for char in t :
        if char in seen_t :
            seen_t[char] += 1
        else :
            seen_t[char] = 1
    print(seen_s)
    print(seen_t)
    return seen_t == seen_s


def optimized_isAnagram(s: str, t: str) -> bool:
    character_count_s = {}
    character_count_t = {}

    for char in s:
        if char in character_count_s:
            character_count_s[char] += 1
        else:
            character_count_s[char] = 1

    for char in t:
        if char in character_count_t:
            character_count_t[char] += 1
        else:
            character_count_t[char] = 1

    return character_count_s == character_count_t


if __name__ == "__main__" :
    print(isAnagram(s = "anagram", t = "nagaram"))