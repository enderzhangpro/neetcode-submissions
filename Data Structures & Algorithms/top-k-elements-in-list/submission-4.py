class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        keys = []
        for i in nums:
            if i in freqDict:
                freqDict[i] += 1
            else:
                keys.append(i)
                freqDict[i] = 1

        returnList = []
        
        for i in range(k):
            biggest_key = keys[0]
            most = freqDict[keys[0]]
            for key in keys[1:]:
                if freqDict[key] > most:
                    biggest_key = key
                    most = freqDict[key]
            returnList.append(biggest_key)
            keys.remove(biggest_key)
        
        return returnList