class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        totalWithoutZero = 1
        zeroCount = 0
        for i in nums:
            if i == 0:
                zeroCount += 1
                total *= i
            else:
                totalWithoutZero *= i
                total *= i
        if zeroCount > 1:
            totalWithoutZero = 0
        
        result = []
        for i in nums:
            if i == 0:
                result.append(totalWithoutZero)
            else:
                result.append(int(total / i))
        return result