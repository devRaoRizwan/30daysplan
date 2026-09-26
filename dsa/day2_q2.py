# 347. Top K Frequent Elements
# Medium

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2

# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1

# Output: [1]

# Example 3:

# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

# Output: [1,2]

 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

def topKFrequent(nums: list[int], k: int) -> list[int]:
    frequency = {}

    for num in nums :
        if num not in frequency :
            frequency[num] = 1
        else :
            frequency[num] += 1

    result = []
    for _ in range(k):
        highest_frequency = 0
        most_frequent_number = None
        for number, count in frequency.items():
            if count > highest_frequency:
                highest_frequency = count
                most_frequent_number = number
        result.append(most_frequent_number)
        del frequency[most_frequent_number]
  
    return result

if __name__ == "__main__" :
    print(topKFrequent(nums = [1,2,1,2,1,2,3,1,3,2], k = 2))