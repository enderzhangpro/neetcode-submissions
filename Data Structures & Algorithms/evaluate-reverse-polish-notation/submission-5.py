class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i].isnumeric() or tokens[i][1:].isnumeric():
                stack.append(int(tokens[i]))
            else:
                result = 0
                # print(stack, tokens[i], tokens[i + 1:])
                if tokens[i] == "+":
                    result += (stack[-2] + stack[-1])
                elif tokens[i] == "-":
                    result += (stack[-2] - stack[-1])
                elif tokens[i] == "*":
                    result += (stack[-2] * stack[-1])
                else:
                    # print(stack[-1], stack[-2])
                    result += int(stack[-2] / stack[-1])
                stack.pop(-1)
                stack.pop(-1)
                stack.append(result)
                print(stack)
        return stack[-1]