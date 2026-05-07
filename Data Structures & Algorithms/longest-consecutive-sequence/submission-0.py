class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(list(set(nums)))
        
        longest = 1

        for i in nums:
            if i - 1 not in nums:
                length = 1
                while (i + length) in nums:
                    length += 1
                longest = max(longest, length)
        return longest