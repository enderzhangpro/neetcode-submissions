class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            count = 1
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    break
                count += 1
            else:
                count = 0
            result.append(count)
        return result