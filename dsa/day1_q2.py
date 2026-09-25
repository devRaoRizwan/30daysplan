# 217. Contains Duplicate
# Easy

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]

# Output: true

 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109


def containsDuplicate(nums: list[int]) -> bool:
    unique_nums = {}
    for i in range(len(nums)):
        if nums[i] in unique_nums:
            return True
        else :
            unique_nums[nums[i]] = 1
    return False


def optimized_containsDuplicate(nums: list[int]) -> bool:
    seen_numbers = {}

    for number in nums:
        if number in seen_numbers:
            return True

        seen_numbers[number] = 1

    return False


if __name__ == "__main__" :
    print(containsDuplicate(nums = [1,2,3,1]))