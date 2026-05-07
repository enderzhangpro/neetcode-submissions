class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        s = s.lower()
        while i < j:
            while not s[i].isalnum():
                i += 1
                if i > j:
                    return True
            while not s[j].isalnum():
                j -= 1
                if i > j:
                    return True
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True