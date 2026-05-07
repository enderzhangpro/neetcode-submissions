class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set(nums)
        if len(set(nums)) != len(nums):
            return True
        return False