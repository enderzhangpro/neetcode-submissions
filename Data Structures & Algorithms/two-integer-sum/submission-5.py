class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNums = []
        for i, num in enumerate(nums):
            sortedNums.append([num, i])
        sortedNums.sort()
        i = 0
        j = len(sortedNums) - 1
        while True:
            if sortedNums[i][0] + sortedNums[j][0] == target:
                return sorted( [sortedNums[i][1], sortedNums[j][1]] )
            elif sortedNums[i][0] + sortedNums[j][0] < target:
                i += 1
            else:
                j -= 1