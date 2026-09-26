# 383. Ransom Note
# Easy

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 

# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.


def canConstruct( ransomNote: str, magazine: str) -> bool:
    ransomNote_dict = {}
    magazine_dict = {}

    for i in ransomNote :
        if i not in ransomNote_dict:
            ransomNote_dict[i] = 1
        else :
            ransomNote_dict[i] += 1

    for i in magazine :
            if i not in magazine_dict:
                magazine_dict[i] = 1
            else :
                magazine_dict[i] += 1

    for letter , count in ransomNote_dict.items():
         if letter not in magazine_dict :
              return False
         if magazine_dict[letter] < count :
              return False
    return True
    


if __name__ == "__main__" :
    print(canConstruct(ransomNote = "a", magazine = "b"))