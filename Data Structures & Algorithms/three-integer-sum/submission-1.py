class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            j = i + 1
            k = len(nums) - 1
            while j < k:
                # print(nums[i], nums[j], nums[k])
                if nums[i] + nums[j] + nums[k] == 0:
                    entry = [nums[i], nums[j], nums[k]]
                    if entry not in res:
                        res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return res