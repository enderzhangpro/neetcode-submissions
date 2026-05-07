class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        water = [0] * len(height)
        tolerance = 0
        while i < len(height) and tolerance < 10:
            tolerance += 1
            if height[i] == 0:
                i += 1
                continue
            for j in range(i + 1, len(height)):
                if height[j] > 0:
                    for k in range(i + 1, j):
                        if water[k] < min(height[i], height[j]):
                            water[k] = max(min(height[i], height[j]) - height[k], 0)
                if height[i] <= height[j]:
                    i = j
                    break
        print(water)
        maxA = sum(water)
        return maxA