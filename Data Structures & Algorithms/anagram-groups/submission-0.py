class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaGramDict = {}
        returnList = []
        count = -1
        for i in strs:
            i_sort = "".join(sorted(i))
            if i_sort in anaGramDict:
                returnList[anaGramDict[i_sort]].append(i)
            else:
                count += 1
                returnList.append([])
                anaGramDict[i_sort] = count
                returnList[count].append(i)
        return returnList