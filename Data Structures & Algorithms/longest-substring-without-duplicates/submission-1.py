class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        substring = [s[0]]
        i = 1
        longest = 1
        while i < len(s):
            if s[i] in substring:
                while True:
                    popped = substring.pop(0)
                    if popped == s[i]:
                        break
            substring.append(s[i])
            if len(substring) > longest:
                longest = len(substring)
            i += 1
        return longest
