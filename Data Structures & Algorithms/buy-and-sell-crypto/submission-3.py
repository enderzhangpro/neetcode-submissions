class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum = prices[0]
        for i in prices[1:]:
            profit = max(profit, i - minimum)
            if i < minimum:
                minimum = i
        return profit