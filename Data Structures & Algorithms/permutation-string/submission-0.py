class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check = []
        for i in s1:
            check.append(i)
        check.sort()
        
        for i in range(len(s2)):
            if s2[i] in check:
                cut = s2[i:i + len(s1)]
                if sorted(cut) == check:
                    return True
        return False