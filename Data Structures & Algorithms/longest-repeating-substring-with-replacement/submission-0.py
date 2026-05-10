class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        freqDict = {}
        longest = 0
        res = 0
        for i in range(len(s)):
            freqDict[s[i]] = 1 + freqDict.get(s[i], 0)
            longest = max(longest, freqDict[s[i]])

            while (i - start + 1) - longest > k:
                freqDict[s[start]] -= 1
                start += 1
            res = max(res, i - start + 1)
        
        return res
