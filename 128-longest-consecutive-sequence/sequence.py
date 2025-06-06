"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

Approach:
- Uses a set for O(1) lookups.
- For each number, checks if it is the start of a sequence.
- Counts the length of each consecutive sequence and returns the maximum found.

Example usage:
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
    print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))  # Output: 9
    print(Solution().longestConsecutive([1,0,1,2]))              # Output: 3
"""

class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        max_len = 0
        for num in num_set:
            if num - 1 not in num_set:
                current = num
                seq_len = 1
                while current +1 in num_set:
                    current += 1
                    seq_len += 1
                max_len = max(max_len, seq_len)
        return max_len
