class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def area(heights, i, j):
            return min(heights[i], heights[j]) * (j - i)
        maxHeight = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                maxHeight = max(maxHeight, area(heights, i, j))
        return maxHeight