# Problem: Find two numbers in array that add up to target
# LeetCode #1 - Two Sum
# Date: June 2026

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]