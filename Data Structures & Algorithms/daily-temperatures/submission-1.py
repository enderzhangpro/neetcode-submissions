class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            print(stack, result)
            if len(stack) > 0:
                while len(stack) > 0 and stack[-1][0] < temperatures[i]:
                    result[stack[-1][1]] = i - stack[-1][1]
                    stack.pop(-1)
            stack.append((temperatures[i], i))
            
        return result